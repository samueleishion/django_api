from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'flappyworld.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'content.views.index', name="index"), 
    url(r'^api/', 'content.views.api', name="api"), 
    url(r'^api/languages/<languages_id>[0-9]$', 'content.views.api', name="api"), 
    # url(r'^api/city/(?P<city_id>\d+)/$', views.api, name='detail'), 
]
