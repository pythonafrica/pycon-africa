from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'home'
urlpatterns = [
    path('', view=views.home, name='home'),
    path('about/',  view=views.about, name='about'),
    path('coc/', view=views.coc, name='coc'),
    path('coc/reporting-guidelines', view=views.reporting, name='reporting'),
    path('coc/guidelines', view=views.guidelines, name='guidelines'),
    path('sponsor/', view=views.sponsor, name='sponsor'),
    
]