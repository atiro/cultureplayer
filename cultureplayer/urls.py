from django.conf.urls import patterns, url
from cultureplayer.views import InstitutionView, LocationView, ObjectView2

urlpatterns = patterns('',
	url(r'^$', InstitutionView.as_view(), name="institutions"),
	url(r'^(?P<institution>\d+)/(?P<decade>\d+)$', ObjectView2, name="objects2"),
#	url(r'^(?P<institution>\d+)/', LocationView.as_view(), name="locations"),
)
