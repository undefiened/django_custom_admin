from django.contrib import admin
from django.db import models
from stats.models import Project, ProjectDetails, Data, Stat

class ProjectDetailsInline(admin.TabularInline):
	model = ProjectDetails
	extra = 0


class ProjectAdmin(admin.ModelAdmin):
	inlines = [
		ProjectDetailsInline,
	]

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectDetails)
admin.site.register(Data)
admin.site.register(Stat)