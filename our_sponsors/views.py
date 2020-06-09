from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import ListView
from django.template import RequestContext
from django.views.generic.detail import DetailView
from .models import *
from .forms import SponsorForm
from hitcount.views import HitCountDetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



# Create your views here.

class SponsorsView(ListView):
    model = Sponsor
    template_name = 'sponsors.html'
    sponsors_list = Sponsor.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super(SponsorsView, self).get_context_data(**kwargs)
        context['sponsors'] = Sponsor.objects.all()
        context['headline'] = Sponsor.objects.filter(category="Headline")
        context['platinum'] = Sponsor.objects.filter(category="Platinum")
        context['diamond'] = Sponsor.objects.filter(category="Diamond")
        context['gold'] = Sponsor.objects.filter(category="Gold")
        context['silver'] = Sponsor.objects.filter(category="Silver")
        context['bronze'] = Sponsor.objects.filter(category="Bronze")
        context['individual'] = Sponsor.objects.filter(category="Individual")
        context['other'] = Sponsor.objects.filter(category="Other")
        
        return context
        

class SponsorsDetailView(HitCountDetailView):
    model = Sponsor
    template_name = 'sponsor_details.html'
    context_object_name = 'sponsor'
    slug_field = 'slug'
    # set to True to count the hit
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super(SponsorsDetailView, self).get_context_data(**kwargs)
        context['sponsor'] = Sponsor.objects.all()
        context.update({
        'popular_sponsors': Sponsor.objects.order_by('-hit_count_generic__hits')[:3],
        })
        return context



def sponsor_new(request):
    if request.method == "POST":
        form = SponsorForm(request.POST)
        if form.is_valid():
            sponsor = form.save(commit=False)
            sponsor.name = request.user
            sponsor.published_date = timezone.now()
            sponsor.save()
            return redirect('sponsor_detail', SponsorsView)
    else:
        form = SponsorForm()
    return render(request, 'sponsor_edit.html', {'form': form})


def sponsor_edit(request, pk):
    sponsor = get_object_or_404(Sponsor, slug)
    if request.method == "POST":
        form = SponsorForm(request.POST, instance=SponsorsView)
        if form.is_valid():
            sponsor = form.save(commit=False)
            sponsor.name = request.user
            sponsor.published_date = timezone.now()
            sponsor.save()
            return redirect('sponsor_detail', SponsorsView)
    else:
        form = SponsorForm(instance=SponsorsView)
    return render(request, 'sponsor_edit.html', {'form': form})


