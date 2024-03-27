from django.conf.urls.static import static
from django.contrib import admin 
from django.urls import include, path, re_path, include
from . import views
from .views import EventView 
from .views import *
from django.conf import settings
from django.contrib.auth.decorators import login_required 
from . import views
from .views import *


app_name = 'event'

urlpatterns = [
    path('', EventListView.as_view(), name='event_list'), 
    path('<slug:slug>/', EventDetailView.as_view(), name='event_detail'), 
    path('<slug:slug>/m/register', EventMentorRegisterView.as_view(), name='mentor_register'), 
    path('<slug:slug>/register', EventRegisterView.as_view(), name='register'),  
    path('update/<int:pk>/edit/', views.event_edit, name='event_edit'),
    re_path('update/(?P<pk>\d+)/', login_required(EventView.as_view()), name='update_event'),  
]
