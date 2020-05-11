from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.


def home(request):
    context = {"home": "active"}
    template = 'home.html'
    return render(request, template, context)


def about(request):
    context = {"about": "active"}
    template = 'about.html'
    return render(request, template, context)


def coc(request):
    context = {"coc": "active"}
    template = 'coc.html'
    return render(request, template, context)


def reporting(request):
    context = {"reporting": "active"}
    template = 'eporting.html'
    return render(request, template, context)


def guidelines(request):
    context = {"guidelines": "active"}
    template = 'guidelines.html'
    return render(request, template, context)


def sponsor(request):
    context = {"sponsor": "active"}
    template = 'sponsor-us.html'
    return render(request, template, context)




def cfp(request):
    context = {"cfp": "active"}
    template = 'cfp.html'
    return render(request, template, context)



def handler404(request, exception):
    return render(request, '404.html', locals())