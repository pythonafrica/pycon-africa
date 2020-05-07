from django_summernote.admin import SummernoteModelAdmin
from  django.contrib import admin
from  .models import Speaker



class SpeakerAdmin(SummernoteModelAdmin):
    summernote_fields = ('bio',)
    

admin.site.register(Speaker, SpeakerAdmin)
