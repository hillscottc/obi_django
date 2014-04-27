from django.conf.urls import patterns, include, url
from obi_app import urls

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'obi_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^obi/', include('obi_app.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
