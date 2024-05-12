from django.db import models
from django.utils import timezone
from registration.models import Profile
from talks.models import Proposal
from event.models import *
from home.models import EventYear


class Day(models.Model):
    conference_day = models.CharField(max_length=30, unique=True, help_text="The name of the conference day (e.g., Day 1, Day 2).")

    class Meta:
        verbose_name = "Conference Day"
        verbose_name_plural = "Conference Days"
        ordering = ['conference_day']

    def __str__(self):
        return self.conference_day


class Room(models.Model):
    room_name = models.CharField(max_length=50, unique=True, default="", null=True, help_text="The name or number of the conference room.")

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
        ordering = ['room_name']

    def __str__(self):
        return self.room_name



DAY_SESSIONS = (
    ('Morning', 'Morning'),
    ('Afternoon', 'Afternoon'),
    ('Evening', 'Evening'),
)

class TalkSchedule(models.Model):
    conference_day = models.ForeignKey(Day, on_delete=models.CASCADE)
    talk = models.ForeignKey(Proposal, on_delete=models.CASCADE, help_text="Select a Talk if it's a Speaker giving a talk")
    is_an_event = models.BooleanField(default=False)
    event = models.CharField(max_length=250, default="", blank=True, help_text="Name of the event [if it's an event]")
    fa_icon = models.CharField(max_length=100, default='', blank=True)
    event_url = models.CharField(max_length=250, default="", blank=True, help_text='URL to the event')
    external_url = models.CharField(max_length=250, default="", blank=True, help_text='External link to the event')
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    day_session = models.CharField(max_length=10, choices=DAY_SESSIONS, default='')
    allocated_room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True, default='')
    rowspan = models.CharField(max_length=10, default='', blank=True, help_text="Use to determine how this talk fits in its time allocation") 
    concurrent_talk = models.BooleanField(default=False)  
    is_a_keynote_speaker = models.BooleanField(default=False)    
    is_a_panel = models.BooleanField(default=False) 

    class Meta:
        managed = True
        verbose_name_plural = "Talk Schedules"

    def __str__(self):
        speakers_names = ', '.join([speaker.user_profile.name for speaker in self.talk.speakers.all()])
        if self.is_an_event:
            return f"{self.event} in {self.allocated_room}"
        return f"{self.talk.title} by {speakers_names}"

 