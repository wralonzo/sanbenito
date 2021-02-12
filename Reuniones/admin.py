from django.contrib import admin
from import_export import resources
from Reuniones.models import Reuniones
from Asistencia.models import Asistencia, Maestro
from import_export.admin import ExportActionMixin


class Exportar(resources.ModelResource):
	class Meta:
		fields=('Fecha','NombreMaestro__Nombres','Descripcion')
		model=Reuniones

class BusquedaReuniones(ExportActionMixin,admin.ModelAdmin):

	resources=Exportar
	list_display=['Fecha','NombreMaestro','Descripcion']
	list_filter	=['Fecha','NombreMaestro','Descripcion']
	search_fields=['Fecha','NombreMaestro__Nombres']
	ordering=['Fecha']
	date_hierarchy='Fecha'


admin.site.register(Reuniones, BusquedaReuniones)
# Register your models here.