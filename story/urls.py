from django.conf.urls import patterns, include, url
from story.views import  editData, playGame, viewUsersStories, createStory

from django.contrib.auth.views import login, logout

from django.contrib import admin
admin.autodiscover()


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	#(r'^admin/$', include(admin.site.urls)),
	(r'^editData/$', editData),
    (r'^playGame/$', playGame),
    (r'^objectView/$', viewUsersStories),
    (r'^createStory/$',createStory),
    (r'^login/$', login),
    (r'^logout/$', logout),

    # Examples:
    # url(r'^$', 'story.views.home', name='home'),
    # url(r'^story/', include('story.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
