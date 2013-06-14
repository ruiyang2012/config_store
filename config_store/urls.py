from django.conf.urls import patterns, include, url
from config_store import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    # url(r'^$', 'config_store.views.home', name='home'),
    url(r'^config_object_def/$', views.ConfigObjectDefinitionList.as_view()),
    url(r'^config_object_def/(?P<pk>[^/]+)/$', views.ConfigObjectDefinitionDetail.as_view()),

    url(r'^config_instance/$', views.ConfigInstanceList.as_view()),
    url(r'^config_instance/(?P<pk>[^/]+)/$', views.ConfigInstanceDetail.as_view()),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
