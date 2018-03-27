from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^main/$', views.main, name='main'),
    url(r'profile/(?P<token>[a-z0-9]+)/$', views.get_user_profile, name='profile'),
    url(r'user/(?P<token>[a-z0-9]+)/$', views.get_logged_in_user, name='user'),
    url(r'stats/(?P<token>[a-z0-9]+)/$', views.get_employee_stats, name='stats'),
    url(r'employees/(?P<token>[a-z0-9]+)/$', views.get_employees, name='employees'),
]