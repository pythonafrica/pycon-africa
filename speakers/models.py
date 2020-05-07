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
    TALK_TYPES = (
        ('Talk', "Talk"),
        ('Tutorial', "Tutorial"),
    )


    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    speaker_name = models.CharField(max_length=200)
    talk_title = models.CharField(max_length=200, default=" ", null=True, blank=True,)
    talk_type = models.CharField(choices=TALK_TYPES, max_length=20,default=" ")
    talk_description = models.TextField(default=" ")
    profile_image = ProcessedImageField(upload_to='speakers/',default="speaker.png", processors=[ResizeToFit(600, 600, upscale=False)], format='jpeg', options={'quality': 90})
    position = models.CharField(max_length=200, help_text="Position of the speaker eg. CEO")
    company = models.CharField(max_length=200, help_text="Name of Organization speaker is from. eg. Google")
    biography = models.TextField()
    bio = models.TextField(null=True, default="", blank=True,)
    twitter = models.CharField(max_length=100, null=True, help_text="Please enter only the user name eg.'mawy_7' ", default="", blank=True,)
    linkedin = models.CharField(max_length=100, null=True, help_text="Please enter only the user name eg. in/mawy7 ", default="", blank=True,)
    website = models.CharField(max_length=100, null=True, default="", blank=True,)
    created_date = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    is_visible = models.BooleanField(default=False)
    published_date = models.DateField(blank=True, null=True)
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