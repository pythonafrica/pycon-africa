from  django.contrib import admin
from  .models import *
from django_summernote.admin import SummernoteModelAdmin
from django.conf import settings
from django.db import models


# Register your models here.
class KeynoteSpeakerAdmin(SummernoteModelAdmin):
    list_display = ("speaker_name", "organization", "created_date", "updated")
    list_filter = ("speaker_name", "organization", "created_date", "updated")
    summernote_fields = '__all__'

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'created_by', None) is None:
            obj.author = request.user
        obj.save()
        
admin.site.register(KeynoteSpeaker, KeynoteSpeakerAdmin)
