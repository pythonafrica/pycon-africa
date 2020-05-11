from  django.contrib import admin
from  .models import Speaker, Talk



class SpeakerAdmin(admin.ModelAdmin):
    list_display = ("speaker_name","created_date", "updated")
    list_filter = ("speaker_name","created_date", "updated")
    



class TalkAdmin(admin.ModelAdmin):
    list_display = ("speaker_name","talk_title", "created_date","updated")
    list_filter = ("speaker_name","created_date","updated")
    

admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Talk, TalkAdmin)
