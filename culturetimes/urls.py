from django.conf.urls import patterns, url
from culturetimes.views import InstitutionView

urlpatterns = patterns('',
	url(r'^$', InstitutionView.as_view(), name="institutions"),
)
