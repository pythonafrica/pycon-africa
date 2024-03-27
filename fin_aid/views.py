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


# Included by me (3rd Parties and more) 
from django.contrib.auth.models import User
from datetime import datetime  
from django.contrib.auth import authenticate, login, get_user_model 
from django.views.generic.edit import UpdateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponseRedirect 

# Fin_aid application imports.
from .models import Fin_aid   
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
 
from fin_aid.mixins import EditOwnFin_aidMixin, EditOwnLoginMixin
from .forms import Fin_aidForm
 
def fin_aid(request):
	fin_aids = Fin_aid.objects.all().order_by('-date_created') 
	return render(request, '2022/fin_aid/fin_aid.html', {'fin_aids': fin_aids})


def fin_aid_edit(request, pk):
    fin_aid = get_object_or_404(Fin_aid, pk=pk)
    if request.method == "POST":
        form = Fin_aidForm(request.POST, instance=fin_aid)
        if form.is_valid():
            fin_aid = form.save(commit=False)
            fin_aid.user = request.user
            fin_aid.date_updated = timezone.now()
            fin_aid.save()
            return redirect('fin_aid:fin_aid_home')
    else:
        form = Fin_aidForm(instance=fin_aid)
    return render(request, '2022/fin_aid/update_fin_aid.html', {'form': form})

 
class Fin_aidView(EditOwnFin_aidMixin, UpdateView):
    form_class = Fin_aidForm
    model = Fin_aid
    template_name = "2022/fin_aid/update_fin_aid.html"
    success_url = reverse_lazy('fin_aid:fin_aid_home')

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Fin_aid'
        context['year'] = datetime.now().year
        try:
            context['fin_aid'] = Fin_aid()
        except Fin_aid.DoesNotExist:
            context['fin_aid'] = ''
        return context

def fin_aid_update_view(UpdateView):
    obj = get_object_or_404(Fin_aid, id=id)
    form = Fin_aidForm(UpdateView.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(UpdateView, "2022/fin_aid/update_fin_aid.html", context)

