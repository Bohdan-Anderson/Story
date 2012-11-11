from django.conf.urls import patterns, include, url
from story.views import hello, viewData, editData, playGame

from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	('^hello/$', hello),
	(r'^admin/', include(admin.site.urls)),
	(r'^viewData/', viewData),
	(r'^editData/', editData),
    (r'^playGame/', playGame)

    # Examples:
    # url(r'^$', 'story.views.home', name='home'),
    # url(r'^story/', include('story.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
