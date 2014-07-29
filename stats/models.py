from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    site = models.CharField(max_length=100)

class ProjectDetails(models.Model)
    project = models.ForeignKey(Project)
    info1 = models.TextField()
    info2 = models.TextField()

class Data(models.Model)
    project = models.ForeignKey(Project)
    field = models,CharField(max_length=100)

class Stat(models.Model)
    data = models.ForeignKey(Data)
    price = models.FloatField()