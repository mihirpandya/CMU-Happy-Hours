from django.conf.urls import patterns, include, url
from happyhours.views import hello_view, get_timings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('django.views.generic.simple',
	url(r'^$', view=hello_view, name='hello_view'),
	url(r'^get_timings', view=get_timings, name='get_timings'),
    # Examples:
    # url(r'^$', 'cmuhappyhours.views.home', name='home'),
    # url(r'^cmuhappyhours/', include('cmuhappyhours.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
