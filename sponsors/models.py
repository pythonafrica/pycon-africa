from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from sponsor_us.models import SponsorshipTier
from home.models import EventYear
from markdownx.models import MarkdownxField 

class Sponsor(models.Model):
    SPONSOR_TYPE = (
        ('C', 'Corporate Sponsor'),
        ('S', 'Special Sponsor'),
        ('D', 'Diversity'),
        ('I', 'Individual Sponsor'),
    )

    name = models.CharField("sponsor name", max_length=200)
    tier = models.ForeignKey(SponsorshipTier, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="sponsorship tier")
    logo = models.ImageField(upload_to="sponsors/", max_length=255, blank=True, null=True)
    sponsor_type = models.CharField("sponsor type", max_length=1, choices=SPONSOR_TYPE)   
    is_visible = models.BooleanField(default=False)
    website = models.URLField(default='', help_text='Link to Sponsor website', blank=True,) 
    twitter = models.CharField(max_length=100, null=True, help_text="Please enter only the user name eg.'mawy_7'", default="", blank=True,)
    linkedin = models.CharField(max_length=100, null=True, help_text="Please enter only the user name eg.'mawy_7'", default="", blank=True,) 
    biography = MarkdownxField(default='', help_text="Description of the Sponsor", blank=True, null=True)
    show_biography = models.BooleanField(default=False, help_text="Untick if the company only want their logo displayed on our website. Not all companies want their information on the site.")
    event_year = models.ForeignKey(EventYear, on_delete=models.CASCADE, default="2024", related_name='sponsors')
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        managed = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('sponsor_detail', kwargs={'year': self.event_year.year, 'slug': self.slug})
 


 

