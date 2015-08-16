from django.conf.urls import patterns, include, url

urlpatterns = patterns('blog.views',
    url(r'^blog/', 'post_list', name='blog_post_list'),
)