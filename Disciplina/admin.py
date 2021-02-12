from django.contrib import admin
from import_export import resources
from Asistencia.models import Alumno, Grado, Maestro, Asistencia
from Disciplina.models import Disciplina
from import_export.admin import ExportActionMixin


class Exportar(resources.ModelResource):
	class Meta:
		fields=('Fecha','NombreAlumno__Nombres','grado_Grado','NombreMaestro__Nombres','Descripcion')
		model=Disciplina
		model=Asistencia


class BusquedaDisciplina(ExportActionMixin,admin.ModelAdmin):

	resources=Exportar
	list_display=['Fecha','NombreAlumno','grado','NombreMaestro','Descripcion']
	list_filter	=['Fecha','NombreAlumno__Nombres','NombreMaestro','Descripcion']
	search_fields=['Fecha','NombreAlumno__Nombres','NombreMaestro__Nombres']
	ordering=['Fecha']
	date_hierarchy='Fecha'




admin.site.register(Disciplina, BusquedaDisciplina)
# Register your models here.