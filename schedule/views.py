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
from .forms import TalkScheduleForm  
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from .models import * 


from datetime import datetime

from .models import TalkSchedule, Day



def schedule(request, year):
    """Renders the schedule page for a specific year."""
    assert isinstance(request, HttpRequest)

    # Fetch the event year or raise 404 if not found
    event_year = get_object_or_404(EventYear, year=year)

    # Check the visibility setting
    visibility = ScheduleVisibility.objects.first()
    if visibility is None:
        visibility = ScheduleVisibility.objects.create(is_live=False)

    # Fetch and order the conference days
    days = Day.objects.all().order_by('conference_day')
    for day in days:
        # Fetch both talks and events for the given day
        day.schedules = TalkSchedule.objects.filter(
            conference_day=day
        ).filter(
            models.Q(talk__event_year=event_year) | models.Q(is_an_event=True)
        ).select_related('talk', 'talk__user').prefetch_related('talk__speakers').order_by('start_time')

    # Meta information for Open Graph and Twitter Cards
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
            'is_schedule_live': visibility.is_live or request.user.is_superuser,
            'meta_title': meta_title,
            'meta_description': meta_description,
            'meta_og_image': meta_og_image,
        }
    )


class ScheduleDetailView(HitCountDetailView):
    model = TalkSchedule
    context_object_name = 'schedule'
    slug_field = 'proposal_id'  # Ensure this field matches your model's field
    count_hit = True  # To count hits for hitcount feature
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
            'schedules': TalkSchedule.objects.filter(talk__event_year=event_year),
            'event_year': event_year
        })
        return context


@login_required
@permission_required('schedule.add_talkschedule', raise_exception=True)
def create_talk_schedule(request, year):
    event_year = get_object_or_404(EventYear, year=year)

    if request.method == 'POST':
        form = TalkScheduleForm(request.POST)
        if form.is_valid():
            talk_schedule = form.save(commit=False)

            # Check if a talk was selected
            if talk_schedule.talk:
                talk_schedule.talk.event_year = event_year  # Only set event_year if a talk is selected
            
            talk_schedule.save()
            return redirect('schedule:schedule', year=year)
    else:
        form = TalkScheduleForm()

    return render(request, f'{year}/schedule/create_schedule.html', {'form': form, 'year': year})
