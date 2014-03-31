from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^(?P<calendar_id>\d+)/$', views.view_calendar, name='view_calendar'),
    url(r'^create_calendar/$', views.create_calendar, name='index'),
    url(r'^$', views.index, name='index'),
)
