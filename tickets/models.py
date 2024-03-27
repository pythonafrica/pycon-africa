from django.db import models

# Create your models here.


from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField 
from django.utils import timezone  

class Ticket(models.Model):
    ticket_title =  models.CharField(max_length=250, null=True, blank=True, help_text='Ticket PyCon Africa')
    ticket_image_one = models.ImageField(help_text="Upload your cover image or leave blank to use our default image",default="tickets.png", null=True, blank=True,
                              upload_to='ticket_page') 
    section_one = MarkdownxField(default='', help_text = "[Supports Markdown] - Ticket PyCon Africa.", null=True, blank=True,
                             )
    section_two = MarkdownxField(default='', help_text = "[Supports Markdown] - Ticket PyCon Africa.", null=True, blank=True,
                             )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, null=True, related_name='ticket_us', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ticket_title

    def get_absolute_url(self):
        return reverse("ticket_home")
 
