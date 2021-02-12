from django.contrib import admin
from import_export import resources
from Asistencia.models import Alumno, Grado, Maestro, Asistencia
from import_export.admin import ExportActionMixin


class Exportar(resources.ModelResource):
	class Meta:
		model=Asistencia
		fields=('Fecha','NombreAlumno__Nombres','grado__NombreGrado','NombreMaestro__Nombres','TipoPermiso','Descripcion')
		exclude = ('id', 'created_at', )
		

class BusquedaInasistencia(ExportActionMixin,admin.ModelAdmin):

	resources=Exportar

	#list_display=['Fecha','NombreAlumno','grado','NombreMaestro','TipoPermiso','Descripcion']
	list_display=['Fecha','NombreAlumno','grado','NombreMaestro','TipoPermiso','Descripcion']
	list_filter	=['Fecha','TipoPermiso']
	search_fields=['Fecha','NombreAlumno__Nombres']
	ordering=['Fecha']
	#date_hierarchy='Fecha'

class BusquedaGrado(admin.ModelAdmin):
	list_display=['NombreGrado']



admin.site.register(Grado,BusquedaGrado)
#admin.site.register(Nivel)
#admin.site.register(Seccion)
admin.site.register(Alumno)
admin.site.register(Maestro)
admin.site.register(Asistencia, BusquedaInasistencia)
# Register your models here.