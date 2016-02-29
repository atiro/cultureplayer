from django.conf.urls import patterns, url
from shakespeare.views import PerformanceView, TalkView, ExcerptsView, OperaView

urlpatterns = patterns('',
	url(r'^$', PerformanceView, name="allview"),
	url(r'^talk$', TalkView, name="talkview"),
	url(r'^opera$', OperaView, name="operaview"),
	url(r'^excerpts$', ExcerptsView, name="excerptsview"),
)
