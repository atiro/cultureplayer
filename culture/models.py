from django.db import models

# Create your models here.

class Institution(models.Model):
	name = models.CharField(max_length=255)
	url = models.URLField()

class Location(models.Model):
	name = models.CharField(max_length=255)
	institution = models.ForeignKey(Institution)

class Object(models.Model):
	title = models.CharField(max_length=255)
	artist = models.CharField(max_length=255, default='')
	location = models.ForeignKey(Location)
	description = models.TextField()
	collection_id = models.CharField(max_length=100)
	url = models.URLField()
	image_url = models.URLField()
