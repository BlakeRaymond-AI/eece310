from django.conf.urls import patterns, include, url
import auth.views
import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'classManager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/$', auth.views.login_user),
    url(r'^register/$', auth.views.register_user),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index)
)
