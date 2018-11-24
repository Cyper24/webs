from django.urls import path, re_path
from django.views.generic import ListView, DetailView
from blog.models import post
from django.views.generic.base import TemplateView

urlpatterns = [
    
    #re_path(r'^(?P<pk>\d+)$', DetailView.as_view(model=post, template_name='post.html')),
    #ListView.as_view(queryset=post.objects.all().order_by("-date")[:25], template_name="index.html"
    
    
]