#home views 
import operator

# Core Django imports.
from django.shortcuts import render, get_object_or_404, redirect 
from django.contrib import messages
from django.db.models import Q 
from django.template import RequestContext
from django.views.generic.detail import DetailView
from django.views.generic import (
    DetailView,
    ListView,
)
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from functools import reduce

# Event application imports.
from .models import Event   
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Included by me (3rd Parties and more) 
from django.contrib.auth.models import User
from datetime import datetime 
from .forms import EventForm

from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.edit import UpdateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponseRedirect 

from hitcount.views import HitCountDetailView
from event.mixins import EditOwnEventMixin, EditOwnLoginMixin

from sponsors.models import Sponsor


 
# Create your views here. 

class EventListView(ListView):
   model = Event
   template_name = '2022/event/event.html'
   paginate_by = 12
   queryset = Event.objects.filter(status=Event.PUBLISHED)
   context_object_name = 'events'
  

class EventDetailView(HitCountDetailView):
    model = Event
    template_name = '2022/event/event_detail.html'
    context_object_name = 'event'
    slug_field = 'slug'
    # set to True to count the hit
    count_hit = True
     

    def get_context_data(self, **kwargs):
        context = super(EventDetailView, self).get_context_data(**kwargs)
        context.update({
        'popular_events': Event.objects.order_by('-hit_count_generic__hits')[:3],
        })
        return context

def event_new(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.published_date = timezone.now()
            event.save()
            return redirect('event_detail', event)
    else:
        form = EventForm()
    return render(request, 'blog/event_edit.html', {'form': form})


def event_edit(request, pk):
    event = get_object_or_404(Event, slug)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.author = request.user
            event.published_date = timezone.now()
            event.save()
            return redirect('event_detail', event)
    else:
        form = EventForm(instance=event)
    return render(request, 'blog/event_edit.html', {'form': form})

def handler404(request, exception):
    return render(request, '404.html', locals())



class EventView(EditOwnEventMixin, UpdateView):
    form_class = EventForm
    model = Event
    template_name = "2022/event/update_event.html"
    success_url = reverse_lazy('event:event_home')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Event'
        context['year'] = datetime.now().year
        try:
            context['event'] = Event()
        except Event.DoesNotExist:
            context['event'] = ''
        return context

def event_update_view(UpdateView):
    obj = get_object_or_404(Event, id=id)
    form = EventForm(UpdateView.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(UpdateView, "2022/event/update_event.html", context)


class EventRegisterView(HitCountDetailView): 
    model = Event
    template_name = '2022/event/event_register.html' 
     
    def get_context_data(self, **kwargs): 
        kwargs['register'] = self.object
        return super().get_context_data(**kwargs)


class EventMentorRegisterView(HitCountDetailView): 
    model = Event
    template_name = '2022/event/event_mentor_register.html' 
     
    def get_context_data(self, **kwargs): 
        kwargs['mentor_register'] = self.object
        return super().get_context_data(**kwargs)