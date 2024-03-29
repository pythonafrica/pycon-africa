from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField 
from django.utils import timezone
from  embed_video.fields  import  EmbedVideoField

from hashids import Hashids
from django.conf import settings 
from hashid_field import HashidAutoField
from hashid_field import HashidField 
from home.models import EventYear
 
 
class CFPSubmissionPeriod(models.Model):
    event_year = models.ForeignKey(EventYear, on_delete=models.CASCADE, default="2024", related_name='submission_periods', help_text="The event year this submission period is for")
    start_date = models.DateTimeField(help_text="Date and time when proposal submissions start")
    end_date = models.DateTimeField(help_text="Date and time when proposal submissions end")

    def __str__(self):
        return f"Submission Period for {self.event_year.year}"

    def is_active(self):
        """Check if the submission period is currently active."""
        now = timezone.now()
        return self.start_date <= now <= self.end_date
    

class Speak(models.Model):
    title =  models.CharField(max_length=250, null=False, blank=False, help_text='Speak at PyCon Africa') 
    content = MarkdownxField(default='', help_text = "[Supports Markdown] - Content for speaking at PyCon Africa.", null=False, blank=False
                             )
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='speak',default=User) 
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    event_year = models.ForeignKey(EventYear, on_delete=models.CASCADE, default="2024", related_name='speaks')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("speak")
 
 

class Proposing_talk(models.Model):
    title =  models.CharField(max_length=250, null=False, blank=False, help_text='Speak at PyCon Africa') 
    content = MarkdownxField(default='', help_text = "[Supports Markdown] - Content.", null=False, blank=False
                             )
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='proposing_talk',default=User) 
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True) 
    event_year = models.ForeignKey(EventYear, on_delete=models.CASCADE, default="2024", related_name='proposing_talks')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("proposing_talk")
 
 

class Recording(models.Model):
    title =  models.CharField(max_length=250, null=False, blank=False, help_text='Recording GL at PyCon Africa') 
    content = MarkdownxField(default='', help_text = "[Supports Markdown] - Content.", null=False, blank=False
                             )
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='recording',default=User) 
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    event_year = models.ForeignKey(EventYear, on_delete=models.CASCADE, default="2024", related_name='recordings')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("recording")
 


class Proposal(models.Model):
    TALK_TYPES = (
        ('Lightning Talk', "Lightning Talk - 5 mins"),
        ('Short Talk', "Short Talk - 30 mins"),
        ('Long Talk', "Long Talk - 45 mins"),
        ('Tutorial', "Tutorial - 2 hours"),
        ('Keynote Speaker', "Keynote Speaker"),
    )

    TALK_CATEGORY = (
        ('GP / Web', "General Python, Web/DevOps"),
        ('GC', "General Community"),
        ('ET', "Emerging Technologies"),
        ('Education', "Education"),
        ('O', "Other"),
    )

    STATUS = (
        ('S', 'Submitted'),
        ('A', 'Accepted'),
        ('W', 'Waiting List'),
        ('R', 'Rejected'),
    )

    PROGRAMMING_EXPERIENCE = (
        ('BGN-L', 'Beginner Level'),
        ('INT-L', 'Intermediate Level'),
        ('EXP-L', 'Expert Level'),
    )

    email = models.EmailField(help_text="It will be kept secretly from the Public")
    title = models.CharField(max_length=1024, help_text="Public title. What topic/project is it all about?")
    talk_type = models.CharField(max_length=50, choices=TALK_TYPES)
    talk_category = models.CharField(max_length=50, choices=TALK_CATEGORY)
    proposal_id = HashidAutoField(primary_key=True, salt=f"talks_proposal{settings.HASHID_FIELD_SALT}", default=None)
    elevator_pitch = MarkdownxField(blank=True, null=True, help_text="[Supports Markdown] - Describe your Talk to your targeted audience.")
    talk_abstract = MarkdownxField(blank=True, null=True, help_text="[Supports Markdown] - Your talk_abstract.")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="proposals", on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=STATUS, default='S')
    intended_audience = models.CharField(max_length=50, choices=PROGRAMMING_EXPERIENCE, blank=True, null=True)
    link_to_preview_video_url = models.URLField(blank=True, help_text='Link to Preview video on your Youtube or Google drive')
    anything_else_you_want_to_tell_us = MarkdownxField(blank=True, null=True, help_text="Kindly add anything else you want to tell us?")
    recording_release = models.BooleanField(default=True)
    youtube_video_url = models.URLField(blank=True, help_text='Link to Talk on youtube Video')
    youtube_iframe_url = models.URLField(max_length=300, blank=True, help_text='Link to Youtube Iframe')
    event_year = models.ForeignKey(EventYear, on_delete=models.CASCADE, default="", related_name='proposals', help_text="The event year this proposal is for")
    
    created_date = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("talk_list")

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)