from django.db import models
from culture.models import Object
from genome.models import Programme

# Create your models here.

class Cast(models.Model):
	name = models.CharField(max_length=255)
	role = models.CharField(max_length=255)

class Performance(models.Model):
	programme = models.ForeignKey(Programme)
	play = models.ForeignKey(Object,default=None,null=True)

class Excerpts(models.Model):
	programme = models.ForeignKey(Programme)
	play = models.ManyToManyField(Object)

class Talk(models.Model):
	programme = models.ForeignKey(Programme)
	play = models.ManyToManyField(Object)

class Childrens(models.Model):
	programme = models.ForeignKey(Programme)
	play = models.ManyToManyField(Object)

class Critical(models.Model):
	programme = models.ForeignKey(Programme)
	play = models.ManyToManyField(Object)

class Opera(models.Model):
	programme = models.ForeignKey(Programme)
	play = models.ForeignKey(Object, default=None,null=True)
