from django.conf import settings
from django.db import models
from django.utils import timezone

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from django_extensions.db.fields import AutoSlugField
from django_slugify_processor.text import slugify
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.encoding import python_2_unicode_compatible


from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
@python_2_unicode_compatible



class Talktype(models.Model):
    talk_type = models.CharField(max_length=20,default="")
    created_date = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """
        Returns string representation on model.
        """
        talktype = f"{self.talk_type}"
        return talktype


class Speaker(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    speaker_name = models.CharField(default="", max_length=200)
    profile_image = ProcessedImageField(upload_to='speakers/',default="speakers/speaker.png", processors=[ResizeToFit(600, 600, upscale=False)], format='jpeg', options={'quality': 90})
    profession = models.CharField(max_length=200, null=True, default="", blank=True, help_text="Speaker's profession. eg. Software Developer")
    country = models.CharField(max_length=100, null=True, default="", blank=True, help_text="City and Country the speaker is from eg. Accra, Ghana")
    biography = models.TextField(max_length=600, null=True, default="", help_text="The bio of the speaker")
    twitter = models.CharField(max_length=100, null=True, help_text="Please enter only the user name eg.'mawy_7' ", default="", blank=True,)
    github = models.CharField(max_length=100, null=True, help_text="Please enter only the user name eg.'mawy_7' ", default="", blank=True,)
    linkedin = models.CharField(max_length=100, null=True, help_text="Please enter only the user name eg.'/mawy_7' ", default="", blank=True,)
    talk_title = models.CharField(max_length=200, default="", null=True)
    talk_type = models.ForeignKey(Talktype, on_delete=models.CASCADE, default="", null=True)
    talk_description = models.TextField(default="")
    beginner_level = models.BooleanField(default=False)
    intermediate_level = models.BooleanField(default=False)
    expert_level = models.BooleanField(default=False)
    youtube_vide_url = models.URLField(default="", blank=True, help_text='Link to Talk on youtube Video')
    youtube_iframe_url = models.URLField(max_length=300,default="", blank=True, help_text='Link to Youtube Iframe')
    created_date = models.DateTimeField(default=timezone.now)
    is_visible = models.BooleanField(default=False)
    published_date = models.DateField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(
        populate_from='speaker_name',
        slugify_function=slugify
    )

    def __str__(self):
        return self.speaker_name
        

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.speaker_name)
        return super(Speaker, self).save(*args, **kwargs)

