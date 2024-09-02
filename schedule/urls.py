from django.urls import path, include
from . import views
from .views import *
  



app_name = 'schedule'
urlpatterns = [
    path('', views.schedule, name='schedule'),
    path('<slug:slug>', ScheduleDetailView.as_view(), name='schedule_detail'), 
    #path('<slug:slug>/edit/', views.schedule_edit, name='schedule_edit'),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
    path('create/', create_talk_schedule, name='create_talk_schedule'),
]