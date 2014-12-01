from django.shortcuts import render
from django.view.generic.list import ListView
from culture import Institution, Location, Object

# Create your views here.

#def LocationView(request, institution, location, date):
	

class InstitutionView(ListView):
	template_name = 'culturetimes/institutions.html'
	context_object_name = 'institution_list'
	model = Institution
