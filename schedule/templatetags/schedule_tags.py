from django import template 
from django.utils import timezone
register = template.Library() 

from datetime import datetime
from ..models import *

from registration.models import Profile 
from talks.models import Proposal

from ..models import TalkSchedule, Day, Event


@register.inclusion_tag('2022/schedule/schedule_home.html')
def show_home_schedule():
    schedule_one = TalkSchedule.objects.filter(conference_day='1').select_related('talk').order_by('start_time')
    schedule_two = TalkSchedule.objects.filter(conference_day='2').select_related('talk').order_by('start_time')
    schedule_three = TalkSchedule.objects.filter(conference_day='3').select_related('talk').order_by('start_time')
    return {
            'title': 'Schedule',
            'message': 'Schedule',
            'year': datetime.now().year,
            'schedule_one': schedule_one,
            'schedule_two': schedule_two,
            'schedule_three': schedule_three,
        }
