from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
     url(r'^admin/sentry/', include('sentry.web.urls')),
     url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    # This is appropriate for the development server but NOT for production
    urlpatterns += patterns('django.contrib.staticfiles.views',
        url(r'^static/(?P<path>.*)$', 'serve'),
    )
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT}),
    )
    #urlpatterns += staticfiles_urlpatterns()

# Standard account and registration URLs
urlpatterns += patterns('',
    url(r'^account/password_reset/$',
        'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^account/password_reset/done/$',
        'django.contrib.auth.views.password_reset_done',
        name='password_reset_done'),
    url(r'^account/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),
    url(r'^account/reset/done/$',
        'django.contrib.auth.views.password_reset_complete',
        name='password_reset_complete'),
)
