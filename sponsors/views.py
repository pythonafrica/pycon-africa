from __future__ import absolute_import
from django.shortcuts import render, reverse
from .models import *
from django.http import HttpRequest, HttpResponseRedirect 
from django.shortcuts import render, get_object_or_404, redirect
from sponsor_us.models import SponsorshipTier
# Create your views here.


def Prospectus(request):
    context = {}
    template = 'prospectus.html'
    return render(request, template, context)


def sponsors(request, year): 
    event_year = get_object_or_404(EventYear, year=year)
    sponsorship_tiers = SponsorshipTier.objects.filter(event_year=event_year).order_by('display_order')
    for tier in sponsorship_tiers:
        tier.sponsors = Sponsor.objects.filter(tier=tier, is_visible=True)
    return render(request, f'{year}/sponsors/sponsors.html', {
        'sponsorship_tiers': sponsorship_tiers,
        'event_year': event_year,
    })




def sponsors_list(request, year):
    event_year = get_object_or_404(EventYear, year=year)
    sponsors = Sponsor.objects.filter(event_year=event_year, is_visible=True).order_by('sponsor_type', 'name')
    context = {
        'sponsors': sponsors,
        'year': year,
    }
    return render(request, f'{year}/sponsors/list.html', context)


def sponsor_detail(request, year, slug):
    sponsor = get_object_or_404(Sponsor, slug=slug, event_year__year=year)
    context = {
        'sponsor': sponsor,
        'year': year,
    }
    return render(request, f'{year}/sponsors/detail.html', context)