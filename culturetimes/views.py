from django.shortcuts import render, render_to_response
from django.views.generic.list import ListView
from django.template import RequestContext
from culture.models import Institution, Location, Object
from genome.models import Programme
from datetime import datetime


# Create your views here.

#def LocationView(request, institution, location, date):
	

class InstitutionView(ListView):
	template_name = 'culturetimes/institutions.html'
	context_object_name = 'institution_list'
	model = Institution

class LocationView(ListView):
	template_name = 'culturetimes/locations.html'
	context_object_name = 'location_list'
	model = Institution

	def get_queryset(self):
		"""
		Return locations for this institution
		"""
		institution = self.kwargs['institution']
		return Location.objects.filter(institution=institution)

class ObjectView(ListView):
	template_name = 'culturetimes/objects.html'
	context_object_name = 'object_list'
	model = Object 

	def get_queryset(self):
		"""
		Return objects for this location
		"""
		location = self.kwargs['location']
		return Object.objects.filter(location=location)

#def programmes(request, institution, location):
#	try:
##		objects

def ObjectView2(request, institution, location):

#	# Order 
	# Create dict indexed by object 
	# obj[id][decade][
	
	loc = Location.objects.get(id=location)
	objs = Object.objects.filter(location=location)

	for obj in objs:
	  programmes = []
	  year = 1920
	  while year < 1990:
	    decade_start = datetime(year,1,1)
	    decade_end = datetime(year + 10,1,1)

	    obj_programmes = obj.programme_set.filter(datetime__range=([decade_start, decade_end]))
	    if len(obj_programmes) > 0:
		programmes.append(obj_programmes[0])
	    else:
		programmes.append(None)

	    year += 10

	  obj.programmes = programmes
	   
	return render_to_response("culturetimes/objects.html",
				 {"object_list": objs,
				  "location": loc},
				 context_instance=RequestContext(request))
