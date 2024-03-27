from os import name
from urllib import request
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.template import RequestContext
from django.views.generic.detail import DetailView
from .forms import SpeakerForm
from django.shortcuts import get_object_or_404
from hitcount.views import HitCountDetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from next_prev import next_in_order, prev_in_order
 
from registration.models import Profile 
from talks.models import Proposal
from schedule.models import TalkSchedule

from event.models import Event


class Speakers(ListView):
   model = Profile
   template_name = '2022/speakers/speaker_list.html'
   context_object_name = 'speakers'
   ordering = ['date_created']

'''

def speakers(request):
    template_name = '2022/speakers/speaker_list.html' 
    speakers = Profile.objects.all()
    talks = Proposal.objects.all()
    context = {
        'nbar': 'resources',
        'Speakers': speakers,
        'Talks': talks,
        }
    return render(request, template_name, context)
'''


class SpeakerDetailView(HitCountDetailView):
    model = Profile
    template_name = '2022/speakers/speaker_details.html'
    context_object_name = 'speaker'
    slug_field = 'slug'
    # set to True to count the hit
    count_hit = True
    paginate_by = 3


    def get_context_data(self, *args, **kwargs):
        context = super(SpeakerDetailView, self).get_context_data(**kwargs)

        context['talks'] = Proposal.objects.filter(user=self.object.user, status="A", 
                                                       )
        
        context['events'] = Event.objects.all()
        
        context['speakers'] = Profile.objects.all()
        context['shedule'] = TalkSchedule.objects.all()
         
        context['related_speakers'] = \
            Profile.objects.filter(is_visible=True,).order_by('?')[:10]

        return context 





def speaker_new(request):
    if request.method == "POST":
        form = SpeakerForm(request.POST)
        if form.is_valid():
            speaker = form.save(commit=False)
            speaker.author = request.user
            speaker.published_date = timezone.now()
            speaker.save()
            return redirect('2022/speakers/speaker_detail', speaker)
    else:
        form = SpeakerForm()
    return render(request, '2022/speakers/speaker_edit.html', {'form': form})


def speaker_edit(request, pk):
    speaker = get_object_or_404(Profile, slug)
    if request.method == "POST":
        form = SpeakerForm(request.POST, instance=speaker)
        if form.is_valid():
            speaker = form.save(commit=False)
            speaker.author = request.user
            speaker.published_date = timezone.now()
            speaker.save()
            return redirect('2022/speakers/speaker_detail', speaker)
    else:
        form = SpeakerForm(instance=speaker)
    return render(request, '2022/speakers/speaker_edit.html', {'form': form})




'''
# default ordering
first = Profile.objects.first()
second = next_in_order(first)
prev_in_order(second) == first # True
last = prev_in_order(first, loop=True)

# custom ordering
qs = Profile.objects.all().order_by('-date_created')
newest = qs.first()
second_newest = next_in_order(newest, qs=qs)
oldest = prev_in_order(newest, qs=qs, loop=True)

'''