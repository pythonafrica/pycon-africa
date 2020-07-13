from  django.contrib import admin
from  .models import *
from django.conf import settings
from django.db import models


# Register your models here.
class KeynoteSpeakerAdmin(admin.ModelAdmin):
    list_display = ("speaker_name", "organization", "created_date", "updated")
    list_filter = ("speaker_name", "organization", "created_date", "updated")
    search_fields = ('speaker_name',)

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'created_by', None) is None:
            obj.author = request.user
        obj.save()
        
admin.site.register(KeynoteSpeaker, KeynoteSpeakerAdmin)
