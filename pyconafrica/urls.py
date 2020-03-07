"""pyconafrica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import handler404, handler500

from pyconafrica2019 import views

urlpatterns = [
    path('', include('home.urls', namespace='home')),
    path('2019/', include('pyconafrica2019.urls', namespace='pyconafrica2019')),
    #path('contact', include('contact_us.urls')),
    path('admin/', admin.site.urls),
]
