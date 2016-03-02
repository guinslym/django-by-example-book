from django.conf.urls import url
from . import views

urlpatterns = [
        # post views
        url(r'^login/$', views.user_login, name='login'),

        ]
