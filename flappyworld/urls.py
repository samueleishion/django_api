from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'flappyworld.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'content.views.index', name="index"), 

    # search 
    url(r'^search/$','content.views.search'), 
    url(r'^search/(?P<query>[a-zA-Z0-9-\s]+)/$','content.views.search'), 

    # api 
    url(r'^api/$', 'content.views.api', name="api"), 

    # list of all objects 
    url(r'^api/cities/$', 'content.views.api_cities', name="api"), 
    url(r'^api/languages/$', 'content.views.api_languages', name="api"), 
    url(r'^api/activities/$', 'content.views.api_activities', name="api"), 

    # particular objects 
    url(r'^api/cities/(?P<city_id>[a-zA-Z0-9-\s]+)/$', 'content.views.api_cities', name="api"), 
    url(r'^api/languages/(?P<lang_id>[a-zA-Z0-9-\s]+)/$', 'content.views.api_languages', name="api"), 
    url(r'^api/activities/(?P<acts_id>[a-zA-Z0-9-\s]+)/$', 'content.views.api_activities', name="api"),  
]
