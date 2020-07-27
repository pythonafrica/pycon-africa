from django.contrib import admin

# Register your models here.
 
from .models import TalkSchedule, Event, Day

class TalkScheduleAdmin(admin.ModelAdmin):
    list_display = ("talk", "conference_day")
    list_filter = ("talk", "conference_day")


admin.site.register(TalkSchedule, TalkScheduleAdmin)
admin.site.register(Event)
admin.site.register(Day)
