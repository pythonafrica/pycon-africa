from django.conf import settings
from django.db import models
from django.utils import timezone

from django_extensions.db.fields import AutoSlugField
from django_slugify_processor.text import slugify
from django.contrib.contenttypes.fields import GenericRelation
  
class Sponsor(models.Model):
    SPONSOR_PACKAGES = (('Headline', 'Headline - $16000'),
                        ('Platinum', 'Platinum - $8000'),
                        ('Diamond', 'Diamond - $4000'),
                        ('Gold', 'Gold - $2000'),
                        ('Silver', 'Silver - 1000'),
                        ('Bronze', 'Bronze - 500'),
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
    url = models.URLField(default='', help_text='Link to Sponsor website', blank=True,)
    description = models.TextField(default='', help_text = "Description of the Sponsor", blank=True, null=True
                             )
    created_date = models.DateTimeField(default=timezone.now)
    is_visible = models.BooleanField(default=False)
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
