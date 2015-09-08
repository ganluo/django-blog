from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog/$', views.archive, name='archive'),
    url(r'^about/$', views.about, name='about'),
    url(r'^category/(?P<name>\w+)/$', views.category, name='category'),
    url(r'^search/$', views.search, name = 'search'),
    url(r'^(?P<year>[0-9]{4})/$', views.year_archive, name='year_archive'),
    url(r'^(?P<year>[0-9]{4})/(?P<month>0[1-9]|1[0-2])/$', views.month_archive, name='month_archive'),
    url(r'^(?P<year>[0-9]{4})/(?P<month>0[1-9]|1[0-2])/(?P<day>[0-3][0-9])/$', views.day_archive, name='day_archive'),
    url(r'^(?P<year>[0-9]{4})/(?P<month>0[1-9]|1[0-2])/(?P<day>[0-3][0-9])/(?P<title>[\S ]+)/$', views.detail, name='detail'),
] 
