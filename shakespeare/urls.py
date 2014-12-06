from django.conf.urls import patterns, url
from shakespeare.views import AllView

urlpatterns = patterns('',
	url(r'^$', AllView, name="allview"),
	url(r'^(?P<institution>\d+)/(?P<location>\d+)$', ObjectView2, name="objects2"),
	url(r'^(?P<institution>\d+)/', LocationView.as_view(), name="locations"),
)
