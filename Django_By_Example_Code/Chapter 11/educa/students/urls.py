from django.conf.urls import url
from . import views

from django.views.decorators.cache import cache_page

urlpatterns = [
    url(r'^register/$', views.StudentRegistrationView.as_view(), name='student_registration'),
    url(r'^enroll-course/$', views.StudentEnrollCourseView.as_view(), name='student_enroll_course'),
    url(r'^courses/$', views.StudentCourseListView.as_view(), name='student_course_list'),
    url(r'^course/(?P<pk>\d+)/$',
        cache_page(60 * 15)(views.StudentCourseDetailView.as_view()),
        name='student_course_detail'),
    url(r'^course/(?P<pk>\d+)/(?P<module_id>\d+)/$',
        cache_page(60 * 15)(views.StudentCourseDetailView.as_view()),
        name='student_course_detail_module'),
]
