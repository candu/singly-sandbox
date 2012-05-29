from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'foo.views.home'),
    url(r'^login$', 'foo.views.login'),
    url(r'^callback$', 'foo.views.callback'),
)
