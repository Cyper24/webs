"""webs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from blog.models import post
from blog import views


urlpatterns = [
    path('inibukanadmin', admin.site.urls),
    path('', ListView.as_view(queryset=post.objects.all().order_by("-date")[:25], template_name="dasbor.html")),
    path('blog/<int:pk>',DetailView.as_view(model=post, template_name='post.html')),
    path('blog/', ListView.as_view(queryset=post.objects.all().order_by("pk"), template_name="blog.html")),
    #path('blog/<int:pk>',ListView.as_view(queryset=post.objects.all().order_by("-date")[:25], template_name="index.html")),
    #path('blog/<int:pk>',ListView.as_view(queryset=post.objects.all().order_by("-date")[:25], template_name="index.html")),
    #DetailView.as_view(model=post, template_name='post.html'),
   


]
