from django.shortcuts import render, render_to_response
from django.views.generic import ListView
from django.template import RequestContext
from django.views.generic.detail import DetailView
# Create your views here.


def home19(request):
    context = {}
    template = 'home19.html'
    return render(request, template, context)

def about(request):
    context = {}
    template = 'about/about19.html'
    return render(request, template, context)

def schedule(request):
    context = {}
    template = 'schedule/schedule19.html'
    return render(request, template, context)

def conduct(request):
    context = {}
    template = 'conduct/conduct19.html'
    return render(request, template, context)

def sponsor_us(request):
    context = {}
    template = 'sponsor/sponsor19.html'
    return render(request, template, context)

def sponsors(request):
    context = {}
    template = 'our-sponsors/sponsors19.html'
    return render(request, template, context)

def register(request):
    context = {}
    template = 'register/register19.html'
    return render(request, template, context)

def traveladvice(request):
    context = {}
    template = 'travel/travel19.html'
    return render(request, template, context)

def fin_aid(request):
    context = {}
    template = 'financial-assistance/fin-aid19.html'
    return render(request, template, context)

def team(request):
    context = {}
    template = 'team/team19.html'
    return render(request, template, context)

def report(request):
    context = {}
    template = 'report/report19.html'
    return render(request, template, context)
