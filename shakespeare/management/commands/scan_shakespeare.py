import os
import requests
import re
from datetime import datetime
from time import sleep

from culture.models import Object,Location
from genome.models import Channel, Programme
from shakespeare.models import Performance, Excerpts, Talk, Childrens, Critical, Opera
from django.core.management.base import NoArgsCommand, CommandError

query_cache = {}

class Command(NoArgsCommand):
        help = "Loads objects from json data"

	def handle_noargs(self, **options):

	  for obj in Object.objects.filter(location=72):
	    print "Scanning ", obj.title
	    for prog in obj.programme_set.all():
		
		# Scan title & description for clues!
		if re.match(".*opera.*", prog.description,re.IGNORECASE):
		  opera, created = Opera.objects.get_or_create(programme=prog,play=obj)
		elif re.match(".*(talk|background).*", prog.description,re.IGNORECASE):
		  talk, created = Talk.objects.get_or_create(programme=prog)
		  talk.play.add(obj)
		elif re.match(".*(excerpts|scenes).*", prog.description,re.IGNORECASE):
		  excerpts, created = Excerpts.objects.get_or_create(programme=prog)
		  excerpts.play.add(obj)
		elif re.match(".*children.*", prog.description,re.IGNORECASE):
		  childrens, created = Childrens.objects.get_or_create(programme=prog)
		  childrens.play.add(obj)
		else:
		  perf, created = Performance.objects.get_or_create(programme=prog,play=obj)
