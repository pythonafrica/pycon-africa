# Core Django imports.
from __future__ import unicode_literals
import imp 
from django.contrib import admin
from django.contrib.admin.options import TabularInline, StackedInline

# Blog application imports.
from .models import Event   
from registration.admin import SpeakerInline
#from sponsors.admin import SponsorInline
 


class EventAdmin(admin.ModelAdmin):
    list_display = ('event_title', 'start_time', 'end_time', 'date_created' )  
    ordering = ['start_time', '-date_created', ]   
    #inlines = [SponsorInline]

    class Media:
        js = ['js/collapsed-stacked-inlines.js']
    
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        form_field = super().formfield_for_manytomany(db_field, request, **kwargs)
        if db_field.name in [*self.filter_horizontal]:
            form_field.widget.attrs={'size': '80'}
        return form_field
        

# Registers the Event model at the admin backend.
admin.site.register(Event, EventAdmin)

