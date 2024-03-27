from django.db import models
from django.utils import timezone
from registration.models import Profile

from talks.models import Proposal
from event.models import *


DAY_SESSIONS = (
    ('Morning', 'Morning'),
    ('Afternoon', 'Afternoon'),
    ('Evening', 'Evening'),
) 

class Day(models.Model):
    conference_day = models.CharField(max_length=30)

    class Meta:
        managed = True

    def __str__(self):
        return self.conference_day

class Room(models.Model):
    room = models.CharField(max_length=50)

    class Meta: 
        managed = True

    def __str__(self):
        return self.room

class TalkSchedule(models.Model):
    conference_day = models.ForeignKey(Day, on_delete=models.CASCADE)
    talk = models.ForeignKey(Proposal, on_delete=models.CASCADE, null=False, default='', blank=False, help_text="Select a Talk if it's a Speaker giving a talk")
    is_an_event = models.BooleanField(default=False)     
    event = models.CharField(max_length=250, default="", null=False, blank=True, help_text='Name to event')
    fa_icon = models.CharField(max_length=100, default='',blank=True,)
    event_url = models.CharField(max_length=250, default="", null=False, blank=True, help_text='Name to event')
    external_url = models.CharField(max_length=250, default="", null=False, blank=True, help_text='Link to event')
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    day_session = models.CharField(max_length=10, choices=DAY_SESSIONS, default='')
    allocated_room =  models.ForeignKey(Room, on_delete=models.CASCADE, blank=True, default='')
    rowspan = models.CharField(max_length=10, default='', blank=True, help_text="Use to determine how this talk fits in its time allocation") 
    speakers = models.ManyToManyField(
        to="registration.Profile",
        verbose_name='Speaker', blank=True
        )
    concurrent_talk = models.BooleanField(default=False)  
    is_a_keynote_speaker = models.BooleanField(default=False)    
    is_a_panel = models.BooleanField(default=False) 
    class Meta:
        managed = True
        verbose_name_plural = "talk Schedule"

    def __str__(self):
        if not self.talk:
            return str(self.event)
        return str(self.talk)
 


class Event(models.Model):
    name = models.CharField(max_length=50)
    conference_day = models.ForeignKey(Day, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    day_session = models.CharField(max_length=10, choices=DAY_SESSIONS, default='')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, default='')

    class Meta:
        managed = True

    def __str__(self):
        return self.name