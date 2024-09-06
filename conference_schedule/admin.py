from django.contrib import admin
from conference_schedule.models import Schedule, Room, Day, ScheduleVisibility   
from conference_schedule.forms import TalkScheduleForm  
 
from  .models import Schedule   

class TalkScheduleAdmin(admin.ModelAdmin):
    form = TalkScheduleForm  # Use the custom form

    list_display = ('talk', 'event', 'allocated_room', 'conference_day', 'concurrent_talk', 'is_an_event', 'is_a_keynote_speaker', 'is_a_panel', 'start_time', 'end_time')
    list_editable = ['is_an_event', 'concurrent_talk', 'is_a_keynote_speaker', 'is_a_panel']
    ordering = ['-start_time', ]
    
    # Filters to enhance usability
    list_filter = ['conference_day', 'allocated_room', 'is_a_keynote_speaker', 'is_a_panel', 'concurrent_talk']
    
    # Adding search capabilities
    search_fields = ['talk__title', 'event']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('talk', 'allocated_room', 'conference_day')

    # Custom admin actions
    actions = ['mark_as_keynote', 'mark_as_panel']

    def mark_as_keynote(self, request, queryset):
        queryset.update(is_a_keynote_speaker=True)
        self.message_user(request, "Selected talks are now marked as keynote speakers.")

    def mark_as_panel(self, request, queryset):
        queryset.update(is_a_panel=True)
        self.message_user(request, "Selected talks are now marked as panels.")

    mark_as_keynote.short_description = "Mark selected talks as keynote speakers"
    mark_as_panel.short_description = "Mark selected talks as panels"


# Register the new Schedule, Room, and Day models with the admin
admin.site.register(Schedule, TalkScheduleAdmin)
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
