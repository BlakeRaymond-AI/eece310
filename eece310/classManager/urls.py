from django.conf.urls import patterns, url

import views
urlpatterns = patterns('',
    url(r'^calendar/(?P<calendar_id>\d+)/$', views.view_calendar, name='view_calendar'),
    url(r'^calendar/(?P<calendar_id>\d+)/create_event/$', views.create_event, name='create_event'),
    url(r'^event/(?P<event_id>\d+)/post$', views.post_message, name='post_message'),
    url(r'^event/(?P<event_id>\d+)/$', views.view_event, name='view_event'),
    url(r'^create_calendar/$', views.create_calendar, name='create_calendar'),
    url(r'^$', views.index, name='index'),
)
