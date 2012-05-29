from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'foo.views.home'),
    url(r'^auth/(?P<service>\w+)$', 'foo.views.auth'),
    url(r'^callback$', 'foo.views.callback'),
)
