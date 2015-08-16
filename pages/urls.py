from django.conf.urls import patterns, include, url



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'silvanapp.views.home', name='home'),
    url(r'^about/$', 'pages.views.about', name='about_page'),
    url(r'^contact/$', 'pages.views.contact', name='contact_page'),
    url(r'^contact/danke/', 'pages.views.thankyou'),
    
)
