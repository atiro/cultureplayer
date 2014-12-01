from django.conf.urls import patterns, url
from culturetimes.views import InstitutionView, LocationView, ObjectView

urlpatterns = patterns('',
	url(r'^$', InstitutionView.as_view(), name="institutions"),
	url(r'^(?P<institution>\d+)/(?P<location>\d+)', ObjectView.as_view(), name="objects"),
	url(r'^(?P<institution>\d+)/', LocationView.as_view(), name="locations"),
)
