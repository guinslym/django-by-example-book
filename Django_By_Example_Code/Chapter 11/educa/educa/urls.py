from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static
from courses.views import CourseListView


urlpatterns = [
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^course/', include('courses.urls')),
    url(r'^students/', include('students.urls')),
    url(r'^$', CourseListView.as_view(), name='course_list'),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
