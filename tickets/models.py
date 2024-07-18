from django.db import models

# Create your models here. 
from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField 
from django.utils import timezone  
from home.models import EventYear
from PIL import Image
import os

class Ticket(models.Model):
    ticket_title = models.CharField(max_length=250, null=True, blank=False, help_text='Ticket PyCon Africa')
    ticket_image_one = models.ImageField(help_text="Upload your cover image or leave blank to use our default image", default="tickets.png", null=True, blank=True, upload_to='ticket_page') 
    section_one = MarkdownxField(default='', help_text = "[Supports Markdown] - Section One.", null=True, blank=True)
    section_two = MarkdownxField(default='', help_text = "[Supports Markdown] - Section Two", null=True, blank=True)
    embedded_codes = MarkdownxField(default='', help_text = "[Supports Markdown] - If the Ticket Platform allows you to embed the tickets into your site.", null=True, blank=True)
    donation_link = models.CharField(max_length=250, null=True, blank=True, help_text='Donation for PyCon Africa if any')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, null=True, related_name='ticket_us', on_delete=models.CASCADE)
    event_year = models.ForeignKey(EventYear, on_delete=models.CASCADE, default="2024", related_name='tickets')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    thumbnail_url = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.ticket_title

    def save(self, *args, **kwargs):
        super(Ticket, self).save(*args, **kwargs)
        if self.ticket_image_one:
            self.create_thumbnail()

    def create_thumbnail(self):
        if not self.ticket_image_one:
            return
        
        image = Image.open(self.ticket_image_one.path)
        image.thumbnail((300, 300), Image.ANTIALIAS)

        thumb_name, thumb_extension = os.path.splitext(self.ticket_image_one.name)
        thumb_extension = thumb_extension.lower()

        thumb_filename = thumb_name + '_thumb' + thumb_extension

        # Save the thumbnail in the same location as the original image
        thumb_path = os.path.join(settings.MEDIA_ROOT, 'ticket_page', thumb_filename)

        if thumb_extension in ['.jpg', '.jpeg']:
            FTYPE = 'JPEG'
        elif thumb_extension == '.gif':
            FTYPE = 'GIF'
        elif thumb_extension == '.png':
            FTYPE = 'PNG'
        else:
            return  # Unrecognized file type

        # Save thumbnail
        image.save(thumb_path, FTYPE)

        # Save the thumbnail URL in the model
        self.thumbnail_url = os.path.join('ticket_page', thumb_filename)
        super(Ticket, self).save()
    
    @property
    def thumbnail(self):
        if self.thumbnail_url:
            return os.path.join(settings.MEDIA_URL, self.thumbnail_url)
        return os.path.join(settings.STATIC_URL, 'default_image.png')
 