from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('',views.index),
    path('about',TemplateView.as_view(template_name='about.html')),
    path('blog/',TemplateView.as_view(template_name='blog.html')),
    path('login/',TemplateView.as_view(template_name='login.html'))
]