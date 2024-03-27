from __future__ import absolute_import
from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
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
 
from registration.models import Profile 
from talks.models import Proposal


from datetime import datetime

from .models import TalkSchedule, Day, Event

def schedule(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    schedule_one = TalkSchedule.objects.filter(conference_day='1').select_related('talk').order_by('start_time')
    schedule_two = TalkSchedule.objects.filter(conference_day='2').select_related('talk').order_by('start_time')
    schedule_three = TalkSchedule.objects.filter(conference_day='3').select_related('talk').order_by('start_time')

    return render(
        request,
        '2022/schedule/scheduleN.html',
        {
            'title': 'Schedule',
            'message': 'Schedule',
            'year': datetime.now().year,
            'schedule_one': schedule_one,
            'schedule_two': schedule_two,
            'schedule_three': schedule_three,
        }
    )

 

class ScheduleDetailView(HitCountDetailView):
    model = TalkSchedule
    template_name = '2022/schedule/schedule_details.html'
    context_object_name = 'schedule'
    slug_field = 'proposal_id'
    # set to True to count the hit
    count_hit = True
    paginate_by = 3


    def get_context_data(self, *args, **kwargs):
        context = super(ScheduleDetailView, self).get_context_data(**kwargs)

        context['talks'] = Proposal.objects.filter(status="A",)
        context['speakers'] = Profile.objects.all()
        context['schedules'] = TalkSchedule.objects.all()
         

        return context 


