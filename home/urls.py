from django.urls import path, include
from django.views.generic import TemplateView
from .views import *

from . import views


app_name = 'home'
urlpatterns = [
    path('', Home.as_view(), name='keynotes'),
    path('keynote/<slug:slug>', KeynoteDetailView.as_view(), name='keynote_details'),
    path('new/', views.keynote_new, name='keynote_new'),
    path('<slug:slug>/edit/', views.keynote_edit, name='keynote_edit'),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
    path('about/',  view=views.about, name='about'),
    path('coc/', view=views.coc, name='coc'),
    path('coc/reporting-guidelines', view=views.reporting, name='reporting'),
    path('coc/guidelines', view=views.guidelines, name='guidelines'),
    path('sponsor-us/', view=views.sponsor, name='sponsor'),
    path('sponsor/', view=views.sponsor, name='sponsor'),
    path('tickets/', view=views.tickets, name='tickets'),
    path('team/', view=views.team, name='team'),
    
]