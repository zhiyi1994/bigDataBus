from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'untitled.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^helloworld/', include('helloworld.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
