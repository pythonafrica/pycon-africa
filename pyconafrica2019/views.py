from django.shortcuts import render, render_to_response
from django.views.generic import ListView
from django.template import RequestContext
from django.views.generic.detail import DetailView
# Create your views here.


def home19(request):
    context = {}
    template = 'home19.html'
    return render(request, template, context)

