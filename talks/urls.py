from rest_framework import routers
from django.urls import include, path, re_path
from talks.views import TalkViewsSets 
from django.contrib.auth.decorators import login_required
from talks import views
from .views import *
from django.conf.urls.static import static 
from django.conf import settings

app_name = 'talks'
router = routers.DefaultRouter()
router.register(r'talks', TalkViewsSets)

urlpatterns = [
    # For listing all accepted talks (not year-specific)
    path('accepted_talks/', login_required(views.AcceptedTalksView.as_view()), name='accepted_talks'),
    
    # Submission for a specific year
    path('submit_talk/', login_required(views.submit_talk), name='submit_talk'), 

    # Editing a talk, assuming pk is sufficient for identifying the talk  
    path('<str:pk>/edit_talk/', login_required(views.edit_talk), name='edit_talk'),
    # For listing talks submitted by the logged-in user (not year-specific)
    path('talk_list/', login_required(views.TalkList.as_view()), name='talk_list'), 
    

    # Detail views for talks<int:year>/talks/<int:pk>/talk_details/
    path('<str:pk>/talk_details/', login_required(views.TalkDetailView.as_view()), name='talk_details'), 
    re_path(r'^(?P<pk>[\w-]+)/detail/$', login_required(views.TalksDetailView.as_view()), name='talk_detail'),

    path('<int:year>/talks/success/', SuccessView.as_view(), name='talks_success'),

    # Updated paths to include the year
    path('<int:year>/speaking/', views.speaking, name='speaking'),
    path('<int:year>/proposing_a_talk/', views.proposing, name='proposing'),
    path('<int:year>/recording/', views.recording, name='recording'),
    
    # Redirects for accessing without specifying a year
    path('speaking/', views.speaking, name='speaking_current_year'),
    path('recording/', views.recording, name='recording_current_year'),
    path('proposing_a_talk/', views.proposing, name='proposing_current_year'), 


    path('submitted', login_required(views.SuccessView.as_view()), name='submitted'),
    path('uploads', views.home, name='home'), 
    path('uploads_simple', views.simple_upload, name='simple_upload'),
    path('uploads_form', views.model_form_upload, name='model_form_upload'),
    ]

urlpatterns += router.urls
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

