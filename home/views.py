from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import ListView
from django.template import RequestContext
from django.views.generic.detail import DetailView
from .forms import KeynoteSpeakerForm
from hitcount.views import HitCountDetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from next_prev import next_in_order, prev_in_order

from .models import *
from .models import KeynoteSpeaker
# Create your views here.


class Home(ListView):
    model = KeynoteSpeaker
    context = {"home": "active"}
    template_name = 'home.html'
    context_object_name = 'keynotes'


class KeynoteDetailView(HitCountDetailView):
    model = KeynoteSpeaker
    template_name = 'keynote_detail.html'
    context_object_name = 'keynote'
    slug_field = 'slug'
    # set to True to count the hit
    count_hit = True
    paginate_by = 1
 

    def get_context_data(self, **kwargs):
        context = super(KeynoteDetailView, self).get_context_data(**kwargs)
        context.update({
        'popular_keynotes': KeynoteSpeaker.objects.order_by('-hit_count_generic__hits')[:3],
        })
        return context




def keynote_new(request):
    if request.method == "POST":
        form = KeynoteSpeakerForm(request.POST)
        if form.is_valid():
            keynote = form.save(commit=False)
            keynote.author = request.user
            keynote.published_date = timezone.now()
            keynote.save()
            return redirect('keynote_details', keynote)
    else:
        form = KeynoteSpeakerForm()
    return render(request, 'keynote_edit.html', {'form': form})


def keynote_edit(request, pk):
    keynote = get_object_or_404(KeynoteSpeaker, slug)
    if request.method == "POST":
        form = KeynoteSpeakerForm(request.POST, instance=keynote)
        if form.is_valid():
            keynote = form.save(commit=False)
            keynote.author = request.user
            keynote.published_date = timezone.now()
            keynote.save()
            return redirect('keynote_details', keynote)
    else:
        form = KeynoteSpeakerForm(instance=keynote)
    return render(request, 'keynote_edit.html', {'form': form})




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



def speakers(request):
    context = {"speakers": "active"}
    template = 'speaker_list.html'
    return render(request, template, context)




def tickets(request):
    context = {"tickets": "active"}
    template = 'tickets.html'
    return render(request, template, context)



def team(request):
    context = {"about": "active"}
    template = 'team.html'
    return render(request, template, context)


def handler404(request, exception):
    return render(request, '404.html', locals())

