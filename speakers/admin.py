from  django.contrib import admin
from  .models import *




class TalktypeAdmin(admin.ModelAdmin):
    list_display = ("talk_type", "created_date")
    list_filter = ("talk_type", "created_date")



class SpeakerAdmin(admin.ModelAdmin):
    list_display = ("speaker_name", "talk_title", "talk_type", "created_date", "updated")
    list_filter = ("speaker_name", "talk_title", "talk_type", "created_date", "updated")
    search_fields = ('speaker_name',)
    




admin.site.register(Talktype, TalktypeAdmin)
admin.site.register(Speaker, SpeakerAdmin)