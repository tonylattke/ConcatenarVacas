from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from SistemaVentas.acounts import urls


admin.autodiscover()

urlpatterns = patterns('',
    url(r'' , include(urls)),
    
    
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        
        url(r'^templates/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.TEMPLATE_DIRS[0],
        }),
    )
