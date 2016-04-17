from django.conf.urls import patterns, include, url

#Sitemap
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap

sitemaps = {
        'posts': PostSitemap,
        }


from django.contrib import admin
admin.autodiscover()



urlpatterns =[ 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls', namespace='blog', app_name='blog')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps':sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
