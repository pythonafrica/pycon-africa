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

from home.models import EventYear  
from event.models import Event 
from django.db.models import Q, F, Exists, OuterRef




class Speakers(ListView):
    model = Profile
    context_object_name = 'speakers'
    ordering = ['date_created']

    def get_template_names(self):
        year = self.kwargs.get('year', 'default')
        return [f'{year}/speakers/speaker_list.html']

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filter speakers who have at least one proposal with status 'A' (Accepted)
        # and user_response is 'A' (Accepted by the user)
        queryset = queryset.filter(
            Q(user__proposals__status='A', user__proposals__user_response='A') |
            Q(user__speaking_proposals__status='A', user__speaking_proposals__user_response='A')
        ).distinct().annotate(
            is_keynote_speaker=Exists(
                Proposal.objects.filter(
                    user=OuterRef('user'),
                    talk_type="Keynote Speaker",
                    status='A',
                    user_response='A'
                )
            )
        )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        speakers = context['speakers']
        keynote_speakers = speakers.filter(is_keynote_speaker=True)
        other_speakers = speakers.exclude(is_keynote_speaker=True)
        context.update({
            'keynote_speakers': keynote_speakers,
            'other_speakers': other_speakers
        })
        return context





class SpeakerDetailView(HitCountDetailView):
    model = Profile
    context_object_name = 'speaker'
    slug_field = 'profile_id'
    pk_url_kwarg = 'profile_id'
    count_hit = True

    def get_template_names(self):
        year = self.kwargs.get('year', 'default')
        return [f'{year}/speakers/speaker_details.html']

    def get_context_data(self, **kwargs):
        context = super(SpeakerDetailView, self).get_context_data(**kwargs)
        year = self.kwargs.get('year')
        event_year = get_object_or_404(EventYear, year=year)

        # Get accepted talks for the speaker
        talks = Proposal.objects.filter(user=self.object.user, status="A", event_year=event_year)

        # Collect related speakers without duplication
        related_speakers = Profile.objects.filter(
            is_visible=True,
            user__proposals__status='A',  # Ensure the proposals are accepted
            user__proposals__event_year=event_year
        ).annotate(
            user_accepted=Exists(
                Proposal.objects.filter(
                    user=OuterRef('user'),
                    user_response='A',
                    status='A',
                    event_year=event_year
                )
            )
        ).filter(user_accepted=True).exclude(profile_id=self.object.profile_id).distinct()

        context.update({
            'talks': talks,
            'related_speakers': related_speakers,
            'events': Event.objects.all(),
            'speakers': Profile.objects.filter(is_visible=True),
            'schedule': TalkSchedule.objects.all(),
        })
        return context
