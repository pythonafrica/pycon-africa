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
 



 
class Speaker(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    speaker_name = models.CharField(max_length=200)
    profile_image = ProcessedImageField(upload_to='speakers/',default="default.png", processors=[ResizeToFit(600, 600, upscale=False)], format='jpeg', options={'quality': 90})
    biography = models.TextField(max_length=600, null=True, default="", help_text="The bio of the speaker")
    company = models.CharField(max_length=200, null=True, default="", blank=True, help_text="Name of Organization speaker is from. eg. Google")
    twitter = models.CharField(max_length=100, null=True, help_text="Please enter only the user name eg.'mawy_7' ", default="", blank=True,)
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


 
class Talk(models.Model):
    TALK_TYPES = (
        ('Talk', "Talk"),
        ('Tutorial', "Tutorial"),
    )
    
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    speaker_name = models.ForeignKey(Speaker, on_delete=models.CASCADE)
    talk_title = models.CharField(max_length=200, default="", null=True, blank=True,)
    talk_type = models.CharField(choices=TALK_TYPES, max_length=20,default="")
    talk_abstract = models.TextField(default="")
    talk_description = models.TextField(default="")
    created_date = models.DateTimeField(default=timezone.now)
    is_visible = models.BooleanField(default=False)
    published_date = models.DateField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(
        populate_from='talk_title',
        slugify_function=slugify
    )

    def __str__(self):
        return self.talk_title
        

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.talk_title)
        return super(Talk, self).save(*args, **kwargs)

