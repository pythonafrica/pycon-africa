from django.contrib import admin
from .models import *
from .forms import TalkScheduleForm

class TalkScheduleAdmin(admin.ModelAdmin):
    form = TalkScheduleForm  # Use the custom form

    list_display = ('talk', 'event', 'allocated_room', 'conference_day', "concurrent_talk", "is_a_keynote_speaker", "is_a_panel", 'start_time', 'end_time')
    ordering = ['-start_time', ]
    list_editable = ["concurrent_talk", "is_a_keynote_speaker", "is_a_panel"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('talk', 'allocated_room', 'conference_day')

admin.site.register(TalkSchedule, TalkScheduleAdmin)
admin.site.register(Room)
admin.site.register(Day)


@admin.register(ScheduleVisibility)
class ScheduleVisibilityAdmin(admin.ModelAdmin):
    list_display = ('is_live',)
    actions = ['make_live', 'make_not_live']

    def make_live(self, request, queryset):
        queryset.update(is_live=True)
        self.message_user(request, "The schedule is now live and visible to all users.")

    def make_not_live(self, request, queryset):
        queryset.update(is_live=False)
        self.message_user(request, "The schedule is now hidden from all users except superusers.")

    make_live.short_description = "Make schedule live"
    make_not_live.short_description = "Hide schedule from users"