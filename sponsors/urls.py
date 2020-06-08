from django.urls import path, include
from . import views
from .views import *
 
app_name = 'sponsors'
urlpatterns = [
    path('', views.sponsors, name='sponsors'),
    path('/<slug:slug>', SponsorDetailView.as_view(), name='sponsor_detail'),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
]
