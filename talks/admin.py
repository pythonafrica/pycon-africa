from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

from markdownx.admin import MarkdownxModelAdmin

class TalkAdmin(ImportExportModelAdmin):
    list_display = ("title", "user", "talk_type", "intended_audience", "status", 'created_date', 'date_updated')
    list_editable = ["status"]
    list_filter = ("talk_type",  'created_date', "status")

admin.site.register(Proposal, TalkAdmin)
 
 

class CFPSubmissionPeriodAdmin(admin.ModelAdmin):
    list_display = ('event_year', 'start_date', 'end_date', 'is_active_period')
    list_filter = ('event_year',)
    search_fields = ('event_year__year',)

    def is_active_period(self, obj):
        """Utility method to display if the submission period is currently active."""
        return obj.is_active()
    is_active_period.boolean = True
    is_active_period.short_description = 'Is active?'

admin.site.register(CFPSubmissionPeriod, CFPSubmissionPeriodAdmin)


class SpeakAdmin(admin.ModelAdmin):

    list_display = ('title', 'date_created')  
    ordering = ['-date_created', ]   

# Registers the Cocmodel at the admin backend.
admin.site.register(Speak, SpeakAdmin)


class Proposing_talkAdmin(admin.ModelAdmin):

    list_display = ('title', 'date_created')  
    ordering = ['-date_created', ]   

# Registers the Cocmodel at the admin backend.
admin.site.register(Proposing_talk, Proposing_talkAdmin)


class RecordingAdmin(admin.ModelAdmin):

    list_display = ('title', 'date_created')  
    ordering = ['-date_created', ]   

# Registers the Cocmodel at the admin backend.
admin.site.register(Recording, RecordingAdmin)
 