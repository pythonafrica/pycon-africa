from django.contrib import admin
from .models import *


class SponsorAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "sponsor_type")
    list_filter = ["category", "sponsor_type"]


admin.site.register(Sponsor, SponsorAdmin)
