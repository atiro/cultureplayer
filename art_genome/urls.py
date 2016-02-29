from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'art_genome.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^shakespeare/', include('shakespeare.urls', namespace="shakespeare")),
    url(r'^culturetimes/', include('culturetimes.urls', namespace="culturetimes")),
    url(r'^cultureplayer/', include('cultureplayer.urls', namespace="cultureplayer")),
)
