# Core Django imports.
from django.contrib import admin

# Blog application imports.
from .models import About 
from .models import *

class AboutAdmin(admin.ModelAdmin):
    list_display = ('about_title', 'user',  'event_year', 'date_created')  
    ordering = ['-date_created', ]  
    exclude = ('user',)  # Exclude the user field from the admin form 
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # If the object is being created (and not modified)
            obj.user = request.user  # Set the user to the current user
        super().save_model(request, obj, form, change)

class VenueAdmin(admin.ModelAdmin):
    list_display = ('name',  'event_year', 'date_created')  
    ordering = ['-date_created', ]  
    exclude = ('user',)
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        super().save_model(request, obj, form, change)

class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_title', 'user', 'event_year',  'date_created')  
    ordering = ['-date_created', ]  
    exclude = ('user',)
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        super().save_model(request, obj, form, change)

class TravelAdviceAdmin(admin.ModelAdmin):
    list_display = ('title', 'user',  'event_year', 'date_created')  
    ordering = ['-date_created', ]  
    exclude = ('user',)
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        super().save_model(request, obj, form, change)

class IOCGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'event_year')
    list_filter = ('event_year',)
    search_fields = ('name',)

class IOCMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'event_year')
    list_filter = ('event_year', 'groups')
    search_fields = ('name',)

class VolunteerGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'event_year')
    list_filter = ('event_year',)
    search_fields = ('name',)

class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('name', 'event_year')
    list_filter = ('event_year', 'groups')
    search_fields = ('name',)
 
# Register your models and admin classes
admin.site.register(IOCGroup, IOCGroupAdmin)
admin.site.register(IOCMember, IOCMemberAdmin)
admin.site.register(VolunteerGroup, VolunteerGroupAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Venue, VenueAdmin) 
admin.site.register(Travel_Advice, TravelAdviceAdmin) 