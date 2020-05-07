from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import ListView
from django.template import RequestContext
from django.views.generic.detail import DetailView
from .models import Speaker
from .forms import SpeakerForm
from hitcount.views import HitCountDetailView


class SpeakerListView(ListView):
   model = Speaker
   template_name = 'speaker_list.html'
   context_object_name = 'speakers'

class SpeakerDetailView(HitCountDetailView):
    model = Speaker
    template_name = 'speaker_details.html'
    context_object_name = 'speaker'
    slug_field = 'slug'
    # set to True to count the hit
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super(SpeakerDetailView, self).get_context_data(**kwargs)
        context.update({
        'popular_speakers': Speaker.objects.order_by('-hit_count_generic__hits')[:3],
        })
        return context


def speaker_new(request):
    if request.method == "POST":
        form = SpeakerForm(request.POST)
        if form.is_valid():
            speaker = form.save(commit=False)
            speaker.author = request.user
            speaker.published_date = timezone.now()
            speaker.save()
            return redirect('speaker_detail', speaker)
    else:
        form = SpeakerForm()
    return render(request, 'speaker_edit.html', {'form': form})


def speaker_edit(request, pk):
    speaker = get_object_or_404(Speaker, slug)
    if request.method == "POST":
        form = SpeakerForm(request.POST, instance=speaker)
        if form.is_valid():
            speaker = form.save(commit=False)
            speaker.author = request.user
            speaker.published_date = timezone.now()
            speaker.save()
            return redirect('speaker_detail', speaker)
    else:
        form = SpeakerForm(instance=speaker)
    return render(request, 'speaker_edit.html', {'form': form})
