from django.conf.urls import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'medicalme.views.home', name='home'),
    # url(r'^medicalme/', include('medicalme.foo.urls')),
                       
    url(r'^$', 'medicalme.views.home', name='home'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root', settings.STATIC_ROOT}
    ),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
