# -*- coding: UTF-8 -*-
from datetime import datetime
from random import randint

from django.shortcuts import render, render_to_response
from django.views.generic.list import ListView
from django.template import RequestContext

from culture.models import Institution, Location, Object
from genome.models import Programme


# Create your views here.

#def LocationView(request, institution, location, date):
	

class InstitutionView(ListView):
	template_name = 'cultureplayer/institutions.html'
	context_object_name = 'institution_list'
	model = Institution

class LocationView(ListView):
	template_name = 'cultureplayer/locations.html'
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

def ObjectView2(request, institution, decade):

#	# Order 
	# Create dict indexed by object 
	# obj[id][decade][
	decades = [1920, 1930, 1940, 1950, 1960, 1970,
			 1980, 1990, 2000]
	
	inst = Institution.objects.get(id=institution)
	locs = Location.objects.filter(institution=inst)
	objs = Object.objects.filter(location=locs).filter(image_url__isnull=False).order_by("?")

	listed_objs = []

	for obj in objs[0:200]:
	    programmes = []

	    decade_start = datetime(int(decade),1,1)
	    decade_end = datetime(int(decade) + 10,1,1)

	    obj_programmes = obj.programme_set.filter(datetime__range=([decade_start, decade_end]))

	    if len(obj_programmes) > 0:
	    	obj.programmes = obj_programmes[randint(0, len(obj_programmes) -1)]
		listed_objs.append(obj)

	   
	return render_to_response("cultureplayer/player.html",
				 {"object_list": listed_objs,
				  "decades": decades,
				  "institution": inst,
				  "locations": locs
				 },
				 context_instance=RequestContext(request))
