from django.db import models
from Asistencia.models import Maestro

class Reuniones(models.Model):

	Fecha=models.DateField(auto_now=True, verbose_name='Fecha')
	NombreMaestro=models.ForeignKey(Maestro, verbose_name='Maestro', on_delete=models.CASCADE, null=True)
	Descripcion=models.CharField(max_length=100, verbose_name='Descripción', blank=True)	

	def __str__(self):
			return'{}{}{}'.format(self.Fecha,self.NombreMaestro, self.Descripcion)

	class Meta:
		verbose_name='Reunión'
		verbose_name_plural='Reuniones'