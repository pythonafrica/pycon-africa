from django.urls import path
from . import views

app_name = 'pyconafrica2019'
urlpatterns = [
    path('', view=views.home19, name='home19'),
]