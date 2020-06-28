from django.urls import path
from . import views
from speakers.views import *

app_name = 'schedule'
urlpatterns = [
    path('', views.schedule, name='schedule'),
    path('<slug:slug>', SpeakerDetailView.as_view(), name='speaker_detail'),
]