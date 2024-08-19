from __future__ import absolute_import
from django.shortcuts import render
from django.http import HttpRequest, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.template import RequestContext
from django.views.generic.detail import DetailView 
from django.shortcuts import get_object_or_404
from hitcount.views import HitCountDetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from next_prev import next_in_order, prev_in_order
from home.models import EventYear
from registration.models import Profile 
from talks.models import Proposal


from datetime import datetime

from .models import TalkSchedule, Day

def schedule(request, year):
    """Renders the schedule page for a specific year."""
    assert isinstance(request, HttpRequest)
    try:
        event_year = EventYear.objects.get(year=year)
    except EventYear.DoesNotExist:
        raise Http404("Event year does not exist.")

    days = Day.objects.all().order_by('conference_day')
    for day in days:
        # Fetch schedules along with talk and speaker details
        day.schedules = TalkSchedule.objects.filter(
            conference_day=day,
            talk__event_year=event_year
        ).select_related('talk', 'talk__user').prefetch_related('talk__speakers').order_by('start_time')

    # Meta information
    meta_title = f"Schedule | PyCon Africa {year}"
    meta_description = f"Explore the schedule for PyCon Africa {year}, including keynotes, talks, tutorials, and more. Plan your conference experience with us."
    meta_og_image = "https://res.cloudinary.com/pycon-africa/image/upload/v1722977619/website_storage_location/media/schedule_og_image.png"  # Replace with a suitable image

    return render(
        request,
        f'{year}/schedule/schedule.html',
        {
            'title': 'Schedule',
            'year': year,
            'days': days,
            'meta_title': meta_title,
            'meta_description': meta_description,
            'meta_og_image': meta_og_image,
        }
    )








class ScheduleDetailView(DetailView):
    model = TalkSchedule
    context_object_name = 'schedule'
    slug_field = 'proposal_id'  # Ensure this field matches your model's field
    template_name_field = 'schedule_details_template'

    def get_template_names(self):
        # Assuming each TalkSchedule instance can determine its own template
        if self.object:
            year = self.object.talk.event_year.year
            return [f'{year}/talks/{self.get_template_name_field()}.html']
        return ['schedule/default.html']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['year'] = datetime.now().year  # Add more context as needed
        return context

    def get_template_name_field(self):
        return self.template_name_field
    

    
class ScheduleDetailView(DetailView):
    model = TalkSchedule
    context_object_name = 'schedule'
    slug_field = 'proposal_id'
    # Set to True to count the hit
    count_hit = True
    paginate_by = 3

    def get_template_names(self):
        year = self.kwargs.get('year')
        return [f'{year}/schedule/schedule_details.html']

    def get_context_data(self, **kwargs):
        context = super(ScheduleDetailView, self).get_context_data(**kwargs)
        year = self.kwargs.get('year')
        event_year = get_object_or_404(EventYear, year=year)

        context.update({
            'talks': Proposal.objects.filter(status="A", event_year=event_year),
            'speakers': Profile.objects.filter(user__proposals__event_year=event_year).distinct(),
            'schedules': TalkSchedule.objects.filter(event_year=event_year),
            'event_year': event_year
        })
        return context
