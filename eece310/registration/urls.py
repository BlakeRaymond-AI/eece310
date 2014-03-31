from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^register/$', views.register),
    url(r'^profile/$', views.profile),
)
