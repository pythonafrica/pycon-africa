from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField 
from django.utils import timezone  

class Fin_aid(models.Model):
    title =  models.CharField(max_length=250, null=False, blank=False, help_text='Financial Assistance PyCon Africa') 
    financial_assistance = MarkdownxField(default='', help_text = "[Supports Markdown] - Financial Assistance PyCon Africa.", null=False, blank=False
                             )
    google_form_formfacade_code = models.TextField(default='', help_text='Link to your google form', blank=True,)                
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='fin_aid',default=User) 
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("fin_aid")
 