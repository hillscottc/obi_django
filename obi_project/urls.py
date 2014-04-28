from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Make the obi_app urls root, not a sub dir.
    # url(r'^obi/', include('obi_app.urls')),
    url(r'^', include('obi_app.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
