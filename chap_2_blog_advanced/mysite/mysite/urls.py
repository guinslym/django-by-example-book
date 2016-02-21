from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns =[ 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls', namespace='blog', app_name='blog')),
]
