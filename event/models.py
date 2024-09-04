from sched import scheduler
from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField 
from django.utils import timezone  
from home.models import EventYear 

from django.contrib.contenttypes.fields import GenericRelation
from django_extensions.db.fields import AutoSlugField
from django_slugify_processor.text import slugify
from hitcount.models import HitCountMixin, HitCount 

class Event(models.Model):
    DRAFTED = "DRAFTED"
    PUBLISHED = "PUBLISHED"

    # CHOICES
    STATUS_CHOICES = (
        (DRAFTED, 'Draft'),
        (PUBLISHED, 'Publish'),
    )
    event_title =  models.CharField(max_length=250, null=False, blank=False, help_text='Event PyCon Africa')
    event_image = models.ImageField(help_text="Upload your cover image or leave blank to use our default image",
                              upload_to='event_page', default='event.png') 
    event_description = MarkdownxField(default='', help_text = "[Supports Markdown] - Event description.", null=False, blank=False
                             )
    cost = models.CharField(max_length=250, default="Free", null=False, blank=True, help_text='Event Cost')
    venue = models.CharField(max_length=250, default="(TBD)", null=False, blank=True, help_text='Event Venue')
    website_link = models.URLField(default="", blank=True, help_text='Link to registration form if External')
    registration_link = models.TextField(default="", blank=True, help_text='Link to registration form') 
    is_a_google_form = models.BooleanField(default=False)
    google_form_formfacade_code = models.TextField(default='', help_text='Link to your google form', blank=True,)  
    mentors_form_formfacade_code = models.TextField(default='', help_text='Link to your google form for mentors', blank=True, null=True) 
    organizer = models.CharField(max_length=250, default="(TBD)", null=False, blank=True, help_text='Event Organizer')
    organizer_website = models.URLField(max_length=250, default="", null=False, blank=True, help_text='Event Organizer site')
    section_one = MarkdownxField(default='', help_text = "[Supports Markdown] - Event PyCon Africa.", null=False, blank=False
                             )
    section_two = MarkdownxField(default='', help_text = "[Supports Markdown] - Event PyCon Africa.", null=False, blank=True
                             )
    wsya_section_one = MarkdownxField(default='', help_text = "[Supports Markdown] - Why Should You Attend Event PyCon Africa.", null=False, blank=True
                             )
    wsya_section_two = MarkdownxField(default='', help_text = "[Supports Markdown] - Why Should You Attend Event PyCon Africa.", null=False, blank=True
                             )
    wsya_section_three = MarkdownxField(default='', help_text = "[Supports Markdown] - Why Should You Attend Event PyCon Africa.", null=False, blank=True
                             )
    wsya_section_four = MarkdownxField(default='', help_text = "[Supports Markdown] - Why Should You Attend Event PyCon Africa.", null=False, blank=True
                             )
    have_speakers = models.BooleanField(default=False)     
    speaker_session_title = models.CharField(max_length=250, default="Speakers", null=False, blank=True, help_text='Session Title eg. Speakers, Team, Mentor')
    speaker = models.ManyToManyField(
        to="registration.Profile",
        verbose_name='Speaker', blank=True
        )
    #speaker_one_name = models.CharField(max_length=250, default="", null=False, blank=True, help_text='Speaker Name')
    #twitter_username_one = models.CharField(max_length=250, default="", null=False, blank=True, help_text='Speaker Twitter User Name')
    #speaker_image_one  = models.URLField(default="", blank=True, help_text='Link to image')
    #speaker_two_name = models.CharField(max_length=250, default="", null=False, blank=True, help_text='Speaker Name')
    #twitter_username_two = models.CharField(max_length=250, default="", null=False, blank=True, help_text='Speaker Twitter User Name')
    #speaker_image_two  = models.URLField(default="", blank=True, help_text='Link to image')
    #speaker_three_name = models.CharField(max_length=250, default="", null=False, blank=True, help_text='Speaker Name')
    #twitter_username_three = models.CharField(max_length=250, default="", null=False, blank=True, help_text='Speaker Twitter User Name')
    #speaker_image_three  = models.URLField(default="", blank=True, help_text='Link to image')
    #speaker_four_name = models.CharField(max_length=250, default="", null=False, blank=True, help_text='Speaker Name')
    #twitter_username_four = models.CharField(max_length=250, default="", null=False, blank=True, help_text='Speaker Twitter User Name')
    #speaker_image_four  = models.URLField(default="", blank=True, help_text='Link to image')
    sponsor_session_title = models.CharField(max_length=250, default="Sponsors", null=False, blank=True, help_text='Session Title eg. Sponsor, Support, Thanks')
    have_sponsors = models.BooleanField(default=False)     
    sponsor = models.ManyToManyField(
        to="sponsors.Sponsor",
        verbose_name='Sponsor', blank=True
        ) 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, null=True, related_name='event_us', on_delete=models.CASCADE)  
    schedule = MarkdownxField(default='', help_text = "[Supports Markdown] - Event Schedule.", null=True, blank=True
                             )  
    have_a_confirmed_time = models.BooleanField(default=False)
    start_time = models.DateTimeField(default=timezone.now, null=True, blank=True) 
    end_time = models.DateTimeField(default=timezone.now, null=True, blank=True)
    event_year = models.ForeignKey(EventYear, on_delete=models.CASCADE, default="", related_name='events', help_text="The event year this proposal is for")
    date_published = models.DateTimeField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    slug = AutoSlugField(
        populate_from='event_title',
        slugify_function=slugify
    )
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
     related_query_name='hit_count_generic_relation')

    class Meta:
        unique_together = ("event_title",)
        ordering = ('-date_published',)

    def __str__(self):
        return self.event_title
 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.event_title)
        return super(Event, self).save(*args, **kwargs)
 
  
  