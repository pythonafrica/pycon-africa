from django.db import models
from django.utils import timezone

from speakers.models import Speaker, Talk


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
    talk = models.ForeignKey(Talk, on_delete=models.CASCADE)
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