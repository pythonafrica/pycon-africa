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

# FrequentlyAskedQuestion application imports.
from .models import FrequentlyAskedQuestion 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
 
 
def faq(request):
	faqs = FrequentlyAskedQuestion.objects.all().order_by('-date_created') 
	return render(request, '2022/faq/faq.html', {'faqs': faqs})
  