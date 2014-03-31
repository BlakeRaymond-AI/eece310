from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^(?P<calendar_id>\d+)/$', views.view_calendar),
    url(r'^(?P<calendar_id>\d+)/create_event/$', views.create_event, name='create_event'),
    url(r'^create_calendar/$', views.create_calendar),
    url(r'^$', views.index),
)
