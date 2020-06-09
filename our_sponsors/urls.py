from django.urls import path, include
from . import views
from .views import *
 
app_name = 'our_sponsors'


urlpatterns = [
    path('', SponsorsView.as_view(), name='sponsors'),
    #path('/<slug:slug>', SponsorsDetailView.as_view(), name='sponsor_detail'),
    #path('new/', views.sponsor_new, name='sponsor_new'),
    #path('/<slug:slug>/edit/', views.sponsor_edit, name='sponsor_edit'),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
]
