from django.conf.urls import patterns, include, url
from django.contrib import admin
from feeds import BlogFeed
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'silvanapp.views.home', name='home'),
    url(r'^blog/$', 'blog.views.post_list', name='blog_list'),
    url(r'^blog/rss/$', BlogFeed(), name='rss_feed_blog'),
    url(r'^blog/(?P<slug>[-\w]+)/$','blog.views.view_post', name='view_blog_post'),
    url(r'^projects/$', 'projects.views.project_list', name='project_list'),
    url(r'^projects/(?P<slug>[-\w]+)/$','projects.views.view_project', name='view_project'),
    url(r'^$', 'projects.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
                       #url(r'^$', include('django.contrib.flatpages.urls')),
    url(r'^', include('pages.urls')),
            #url(r'^', include('blog.urls')),
    
)
