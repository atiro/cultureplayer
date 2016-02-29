from datetime import datetime

from django.shortcuts import render, render_to_response
from django.template import RequestContext

from culture.models import Object
from shakespeare.models import Performance, Talk, Excerpts, Opera

# Create your views here.


def AllView(request, type):
	perfs = []
	decades = []
	perf_counts = []
	play_popular = []

	macbeth = Object.objects.get(title="Macbeth")
	midsummer = Object.objects.get(title="Midsummer Night's Dream")
	cleopatra = Object.objects.get(title="Antony and Cleopatra")
	romeo = Object.objects.get(title="Romeo and Juliet")

	year = 1920
	while year < 2000:
	  decade_start = datetime(year, 1, 1)
	  decade_end = datetime(year + 10, 1 , 1)
	  decades.append(year)
	  perfs_decade = []
	  perf_count = None
	  play_count = 0
	  play_most = None
	  count = 0

	  if type == "performance":
		  perf_count = len(Performance.objects.filter(programme__datetime__range=([decade_start, decade_end])))
	  elif type == "talk":
		  perf_count = len(Talk.objects.filter(programme__datetime__range=([decade_start, decade_end])))
	  elif type == "opera":
		  perf_count = len(Opera.objects.filter(programme__datetime__range=([decade_start, decade_end])))
	  elif type == "excerpts":
		  perf_count = len(Excerpts.objects.filter(programme__datetime__range=([decade_start, decade_end])))
	
	  perf_counts.append(perf_count)

	  for play in (macbeth, midsummer, cleopatra, romeo):
		  perf = None
		  if type == "performance":
		    count = len(Performance.objects.filter(play=play).filter(programme__datetime__range=([decade_start, decade_end])))
		    perf = Performance.objects.filter(play=play).filter(programme__datetime__range=([decade_start, decade_end]))[0]

		  elif type == "excerpts":
		    count = len(Excerpts.objects.filter(play=play).filter(programme__datetime__range=([decade_start, decade_end])))
		    perf = Excerpts.objects.filter(play=play).filter(programme__datetime__range=([decade_start, decade_end]))
		    if len(perf) > 0:
			perf = perf[0]

		  elif type == "opera":
		    count = len(Opera.objects.filter(play=play).filter(programme__datetime__range=([decade_start, decade_end])))
		    perf = Opera.objects.filter(play=play).filter(programme__datetime__range=([decade_start, decade_end]))
		    if len(perf) > 0:
			perf = perf[0]

		  elif type == "talk":
		    count = len(Talk.objects.filter(play=play).filter(programme__datetime__range=([decade_start, decade_end])))
		    perf = Talk.objects.filter(play=play).filter(programme__datetime__range=([decade_start, decade_end]))
		    if len(perf) > 0:
			perf = perf[0]
	
		  if perf is not None:
			perfs_decade.append(perf)
		  else:
			perfs_decade.append(None)

		  if count > play_count:
			play_most = play.title
			play_count = count

	  play_popular.append(play_most)
	  perfs.append(perfs_decade)
	  year += 10
	
	dec_perfs = zip(decades, perf_counts, play_popular, perfs)
	
	return render_to_response("shakespeare/shakespeare400.html",
				  {"decade_performances": dec_perfs,
				   "random_img": [1,2,3,4,5],
				   "type": type },
				  context_instance=RequestContext(request))

def PerformanceView(request):
	return AllView(request, "performance")

def TalkView(request):
	return AllView(request, "talk")

def ExcerptsView(request):
	return AllView(request, "excerpts")

def OperaView(request):
	return AllView(request, "opera")
