# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Project(models.Model):
	title = models.CharField(max_length=100)
	site = models.CharField(max_length=100)
	class Meta:
		verbose_name = "Проект"
		verbose_name_plural = "Проекты"
	def __unicode__(self):
		return self.title
		

class ProjectDetails(models.Model):
	project = models.ForeignKey(Project)
	info1 = models.TextField()
	info2 = models.TextField()
	class Meta:
		verbose_name = "Информация о проекте"
		verbose_name_plural = "Информация о проектах"
	def __unicode__(self):
		return self.project.title+str(self.id)

class Data(models.Model):
	project = models.ForeignKey(Project)
	field = models.CharField(max_length=100)
	class Meta:
		verbose_name = "Данные"
		verbose_name_plural = "Данные"
	def __unicode__(self):
		return self.field

class Stat(models.Model):
	data = models.ForeignKey(Data)
	date = models.DateField(auto_now_add=True)
	price = models.FloatField()
	class Meta:
		verbose_name = "Статистика"
		verbose_name_plural = "Статистики"
	def __unicode__(self):
		return self.data.field+str(self.date)