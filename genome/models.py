from django.db import models
from culture.models import Object

# Create your models here.

class Channel(models.Model):
	title = models.CharField(max_length=100)
	
class Programme(models.Model):
	title = models.CharField(max_length=200)
	datetime = models.DateTimeField()
	description = models.TextField()
	channel = models.ForeignKey(Channel)
	genome_url = models.URLField()
	related_objects = models.ManyToManyField(Object)
