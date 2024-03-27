from django.urls import path, include
from . import views
from .views import *
 



app_name = 'speakers'
urlpatterns = [
    #path('', views.speakers, name='speakers'), 
    path('<slug:slug>', SpeakerDetailView.as_view(), name='speaker_detail'),
    path('new/', views.speaker_new, name='speaker_new'),
    path('<slug:slug>/edit/', views.speaker_edit, name='speaker_edit'),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
    path('', Speakers.as_view(), name='speakers'),
]


