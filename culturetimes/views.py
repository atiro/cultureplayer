from django.shortcuts import render
from django.views.generic.list import ListView
from culture.models import Institution, Location, Object
from genome.models import Programme

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
