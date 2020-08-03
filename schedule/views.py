from __future__ import absolute_import
from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect


from datetime import datetime

from .models import TalkSchedule, Day, Event

from speakers.views import *


def schedule(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)

    schedule_one = TalkSchedule.objects.filter(conference_day='1').select_related('talk').order_by('start_time')
    schedule_two = TalkSchedule.objects.filter(conference_day='2').select_related('talk').order_by('start_time')
    schedule_three = TalkSchedule.objects.filter(conference_day='3').select_related('talk').order_by('start_time')
    schedule_four = TalkSchedule.objects.filter(conference_day='4').select_related('talk').order_by('start_time')
    schedule_five = TalkSchedule.objects.filter(conference_day='5').select_related('talk').order_by('start_time')
    schedule_six = TalkSchedule.objects.filter(conference_day='6').select_related('talk').order_by('start_time')

    return render(
        request,
        'schedule.html',
        {
            'title': 'Schedule',
            'message': 'Schedule',
            'year': datetime.now().year,
            'schedule_one': schedule_one,
            'schedule_two': schedule_two,
            'schedule_three': schedule_three,
            'schedule_four': schedule_four,
            'schedule_five': schedule_five,
            'schedule_six': schedule_six,
        }
    )