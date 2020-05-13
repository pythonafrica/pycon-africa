from  django.contrib import admin
from  .models import Speaker
from django_summernote.admin import SummernoteModelAdmin


class SpeakerAdmin(SummernoteModelAdmin):
    list_display = ("speaker_name","talk_title", "created_date", "updated")
    list_filter = ("speaker_name","created_date", "updated")
    summernote_fields = '__all__'

admin.site.register(Speaker, SpeakerAdmin)