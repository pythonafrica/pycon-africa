from django.db import models
from django.utils import timezone

from speakers.models import Speaker


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
 
 
class TalkSchedule(models.Model):
    conference_day = models.ForeignKey(Day, on_delete=models.CASCADE)
    talk = models.ForeignKey(Speaker, on_delete=models.CASCADE)
    talk_url = models.CharField(max_length=50, null=True, help_text="Please enter the url to the speaker talk", default="", blank=True,)
    track_colour = models.CharField(max_length=50, null=True, help_text="Colour to indicate it's track type", default="primary")
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    day_session = models.CharField(max_length=10, choices=DAY_SESSIONS, default='')

    class Meta:
        managed = True
        verbose_name_plural = "talk Schedule"

    def __str__(self):
        return str(self.talk) if self.talk else ''



class Event(models.Model):
    name = models.CharField(max_length=50)
    conference_day = models.ForeignKey(Day, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    day_session = models.CharField(max_length=10, choices=DAY_SESSIONS, default='')

    class Meta:
        managed = True

    def __str__(self):
        return self.name