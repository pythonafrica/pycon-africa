from __future__ import absolute_import
from django.shortcuts import render, reverse
from .models import Sponsor
from django.http import HttpRequest, HttpResponseRedirect

# Create your views here.


def sponsors(request):
    assert isinstance(request, HttpRequest)
    headline = Sponsor.objects.filter(category="Headline")
    platinum = Sponsor.objects.filter(category="Platinum")
    diamond = Sponsor.objects.filter(category="Diamond")
    gold = Sponsor.objects.filter(category="Gold")
    silver = Sponsor.objects.filter(category="Silver")
    bronze = Sponsor.objects.filter(category="Bronze")
    individuals = Sponsor.objects.filter(type="I")

    return render(
        request,
        'sponsors.html',
        {
            'headline': headline,
            'platinum': platinum,
            'diamond': diamond,
            'gold': gold,
            'silver': silver,
            'bronze': bronze,
            'individuals': individuals,
        }
    )
