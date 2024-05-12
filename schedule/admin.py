from django.contrib import admin

# Register your models here.

from .models import TalkSchedule, Room, Day



class TalkScheduleAdmin(admin.ModelAdmin): 
    list_display = ('talk', 'event', 'allocated_room', 'conference_day', "concurrent_talk", "is_a_keynote_speaker", "is_a_panel", 'start_time', 'end_time')  
    ordering = ['-start_time', ]  
    list_editable = ["concurrent_talk", "is_a_keynote_speaker", "is_a_panel",]  


admin.site.register(TalkSchedule, TalkScheduleAdmin)
admin.site.register(Room) 
admin.site.register(Day)
