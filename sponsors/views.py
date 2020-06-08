from __future__ import absolute_import
from django.shortcuts import render, reverse
from .models import Sponsor
from django.http import HttpRequest, HttpResponseRedirect
from hitcount.views import HitCountDetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import SponsorForm
# Create your views here.


def sponsors(request):
    assert isinstance(request, HttpRequest)
    headline = Sponsor.objects.filter(category="Headline")
    platinum = Sponsor.objects.filter(category="Platinum")
    diamond = Sponsor.objects.filter(category="Diamond")
    gold = Sponsor.objects.filter(category="Gold")
    silver = Sponsor.objects.filter(category="Silver")
    bronze = Sponsor.objects.filter(category="Bronze")
    individual = Sponsor.objects.filter(category="Individual")
    other = Sponsor.objects.filter(category="Other")

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
            'individual': individual,
            'other': other,
        }
    )




class SponsorDetailView(HitCountDetailView):
    model = Sponsor
    template_name = 'sponsor_details.html'
    context_object_name = 'sponsor'
    slug_field = 'slug'
    # set to True to count the hit
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super(SponsorDetailView, self).get_context_data(**kwargs)
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
            sponsor.author = request.user
            sponsor.published_date = timezone.now()
            sponsor.save()
            return redirect('sponsor_detail', sponsor)
    else:
        form = SponsorForm()
    return render(request, 'sponsor_edit.html', {'form': form})


def sponsor_edit(request, pk):
    sponsor = get_object_or_404(Sponsor, slug)
    if request.method == "POST":
        form = SponsorForm(request.POST, instance=sponsor)
        if form.is_valid():
            sponsor = form.save(commit=False)
            sponsor.author = request.user
            sponsor.published_date = timezone.now()
            sponsor.save()
            return redirect('sponsor_detail', sponsor)
    else:
        form = SponsorForm(instance=sponsor)
    return render(request, 'sponsor_edit.html', {'form': form})
