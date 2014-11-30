from culture.models import Institution, Location, Object
from django.core.management.base import BaseCommand, CommandError
import os, django
import json


#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapp.settings")
#django.setup()

class Command(BaseCommand):
	args = '<filename>'
	help = "Loads objects from json data"

	def handle(self, *args, **options):
	    culture_file = args[0]

	    va_institution = Institution.objects.get(name="V&A")
	    va_room = Location.objects.get(name="Room 21")

	    with open(culture_file) as json_data:
		data = json.load(json_data)

		for obj in data:
		    o = Object(title=obj["title"], location = va_room,
			description = "", collection_id = obj["object_number"],
			url = "", artist = obj["artist"],
			image_url = obj["primary_image_id"])

		    o.save()
		
	
		
	
