from django.conf.urls import url, include
from . import views

urlpattern = [
  url(r'^$', views.post_list, name='post_list'),
        ]

