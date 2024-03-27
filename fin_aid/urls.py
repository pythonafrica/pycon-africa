from django.urls import path
from . import views

app_name = 'fin_aid'
urlpatterns = [
    path('', views.fin_aid, name='fin_aid')
]