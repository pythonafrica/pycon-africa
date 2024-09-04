from django.db import models
from django.utils import timezone
from registration.models import Profile
from talks.models import Proposal
from event.models import *
from home.models import EventYear 
from django.utils.dateparse import parse_date
from django.core.exceptions import ValidationError
from event.models import Event



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



class TalkSchedule(models.Model):
    DAY_SESSIONS = (
        ('Morning', 'Morning'),
        ('Afternoon', 'Afternoon'),
        ('Evening', 'Evening'),
    )

    conference_day = models.ForeignKey(Day, on_delete=models.CASCADE)
    talk = models.ForeignKey(Proposal, on_delete=models.CASCADE, blank=True, null=True, help_text="Select a Talk if it's a Speaker giving a talk")
    is_an_event = models.BooleanField(default=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, blank=True, null=True, help_text="Select an Event if it's not a Talk")
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
        if self.is_an_event:
            return f"{self.event} in {self.allocated_room}"
        speakers_names = ', '.join([speaker.profile.name for speaker in self.talk.speakers.all()])
        return f"{self.talk.title} by {speakers_names}"

    def clean(self):
        # Validation to ensure either a talk or an event is provided, but not both
        if not self.talk and not self.event:
            raise ValidationError('Either a talk must be selected or an event name must be provided.')
        if self.talk and self.event:
            raise ValidationError('You cannot have both a talk and an event in the same schedule entry.')
        if self.is_an_event and not self.event:
            raise ValidationError('You must provide an event name if this is an event.')

    def save(self, *args, **kwargs):
        self.clean()  # Ensure validation is called
        # Ensure conference_day.conference_day is a date object
        if isinstance(self.conference_day.conference_day, str):
            conference_date = parse_date(self.conference_day.conference_day)
        else:
            conference_date = self.conference_day.conference_day

        # Combine the date with the time for start_time and end_time
        if conference_date:
            self.start_time = timezone.make_aware(
                timezone.datetime.combine(conference_date, self.start_time.time())
            )
            self.end_time = timezone.make_aware(
                timezone.datetime.combine(conference_date, self.end_time.time())
            )

        # If the talk is a special one, you can skip further checks or handle it differently
        if self.talk and self.talk.id in [talk['id'] for talk in TalkScheduleForm.SPECIAL_TALKS]:
            self.event = self.talk.title
            self.talk = None  # Remove the talk since it's not a real proposal

        super().save(*args, **kwargs)



 

class ScheduleVisibility(models.Model):
    is_live = models.BooleanField(default=False, help_text="Indicates if the schedule is live and visible to all users.")

    class Meta:
        verbose_name = "Schedule Visibility"
        verbose_name_plural = "Schedule Visibility"

    def __str__(self):
        return "Live" if self.is_live else "Not Live"