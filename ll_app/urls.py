
"""Defines URL patterns for ll_app"""
from django.conf.urls import url
from . import views

urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),
    
    # Show all topics
    url(r'^topics/$', views.topics, name='topics'),
    
    # Details page for a single topic
    url(r'^topics/(?P<topic_id>[0-9]+)/$', views.topic, name='topic'),
]
