# Core Django imports.
from django.contrib import admin
from .models import *
from markdownx.admin import MarkdownxModelAdmin  


class SponsorshipBenefitInline(admin.StackedInline):
    model = SponsorshipBenefit
    extra = 1

class AdditionalResourceInline(admin.StackedInline):
    model = AdditionalResource
    extra = 1


@admin.register(SponsorUsPage)
class SponsorUsPageAdmin(MarkdownxModelAdmin):
    list_display = ('title', 'user', 'event_year', 'date_created', 'date_updated') 
    exclude = ('user',)  # Exclude the user field from the admin form 
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # If the object is being created (and not modified)
            obj.user = request.user  # Set the user to the current user
        super().save_model(request, obj, form, change)

@admin.register(SponsorshipTier)
class SponsorshipTierAdmin(MarkdownxModelAdmin):
    list_display = ('name', 'display_order', 'amount', 'no_needed', 'no_available', 'colour', 'hex', 'date_created', 'date_updated')
    inlines = [SponsorshipBenefitInline, AdditionalResourceInline]
    search_fields = ['name',]   
    exclude = ('user',)  # Exclude the user field from the admin form 
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # If the object is being created (and not modified)
            obj.user = request.user  # Set the user to the current user
        super().save_model(request, obj, form, change)

# You may or may not need to use MarkdownxModelAdmin for SponsorshipBenefit
# and AdditionalResource if they do not contain MarkdownxFields.
@admin.register(SponsorshipBenefit)
class SponsorshipBenefitAdmin(admin.ModelAdmin):
    list_display = ('description', 'tier')

@admin.register(AdditionalResource)
class AdditionalResourceAdmin(admin.ModelAdmin):
    list_display = ('sponsorship_tier', 'package')



