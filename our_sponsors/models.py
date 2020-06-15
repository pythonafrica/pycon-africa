from django.db import models
from django.conf import settings
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

# Create your models here.


class Sponsor(models.Model):
    SPONSOR_PACKAGES = (('Headline', 'Headline'),
                        ('Platinum', 'Platinum'),
                        ('Diamond', 'Diamond'),
                        ('Gold', 'Gold'),
                        ('Silver', 'Silver'),
                        ('Bronze', 'Bronze'),
                        ('Individual', 'Individual'),
                        ('Other', 'Other'),
                        )

    SPONSOR_TYPE =(('C', 'Corporate Sponsor'),
                   ('S', 'Special Sponsor'),
                   ('I', 'Individual Sponsor'),)

    name = models.CharField("sponsor name", max_length=200)
    category = models.CharField(max_length=15, choices=SPONSOR_PACKAGES)
    logo = models.ImageField(upload_to="sponsors/",max_length=255, blank=True, null=True)
    sponsor_type = models.CharField("sponsor type", default='', max_length=1, choices=SPONSOR_TYPE)
    website = models.URLField(default='', help_text='Link to Sponsor website', blank=True,)
    twitter = models.CharField(max_length=100, null=True, help_text="Please enter only the user name eg.'mawy_7' ", default="", blank=True,)
    linkedin = models.CharField(max_length=100, null=True, help_text="Please enter only the user name eg.'mawy_7' ", default="", blank=True,)
    youtube = models.URLField(max_length=100, null=True, help_text="Please enter organization youtube channel link' ", default="", blank=True,)
    description = models.TextField(default='', help_text = "Description of the Sponsor", blank=True, null=True
                             )
    created_date = models.DateTimeField(default=timezone.now)
    is_visible = models.BooleanField(default=False)
    show_biography = models.BooleanField(default=True, help_text = "Untick if the company only want their logo displayed on our website. Not all companies want their information on the site.",)
    published_date = models.DateField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(
        populate_from='name',
        slugify_function=slugify
    )

    def __str__(self):
        return self.name
        

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Sponsor, self).save(*args, **kwargs)


