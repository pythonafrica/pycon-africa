from  django.contrib import admin
from  .models import *
from django_summernote.admin import SummernoteModelAdmin



class TalktypeAdmin(admin.ModelAdmin):
    list_display = ("talk_type", "created_date")
    list_filter = ("talk_type", "created_date")



class SpeakerAdmin(SummernoteModelAdmin):
    list_display = ("speaker_name", "created_date", "updated")
    list_filter = ("speaker_name","created_date", "updated")
    summernote_fields = '__all__'



class TalkAdmin(SummernoteModelAdmin):
    list_display = ("talk_title", "speaker_name", "talk_type", "created_date", "updated")
    list_filter = ("speaker_name", "talk_type", "created_date", "updated")
    summernote_fields = '__all__'

admin.site.register(Talktype, TalktypeAdmin)
admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Talk, TalkAdmin)