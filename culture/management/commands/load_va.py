from culture.models import Institution, Location, Object
from django.core.management.base import BaseCommand, CommandError
import os, django
import json

class Command(BaseCommand):
	args = '<filename>'
	help = "Recurse through directory loading objects from json data"

	def handle(self, *args, **options):
	    culture_dir = args[0]

	    va_institution = Institution.objects.get(name="V&A")

	    for root, dirs, files in os.walk(args[0]):
	      if "objects.json" not in files:
		continue

	      print "Loading data in: ", os.path.join(root, "objects.json")

	      with open(os.path.join(root, "objects.json")) as json_data:
		data = json.load(json_data)
		location, success = Location.objects.get_or_create(
					institution = va_institution,
					name = data["location"],
					description = data["description"])

		for obj in data["objects"]:
		    o = Object(title=obj["title"], location = location,
			description = "", collection_id = obj["object_number"],
			url = "", artist = obj["artist"],
			image_url = obj["primary_image_id"])

		    o.save()
		
	
		
	
