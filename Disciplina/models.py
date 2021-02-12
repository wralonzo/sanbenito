from django.db import models
from Asistencia.models import Asistencia, Alumno, Maestro, Grado



class Disciplina(models.Model):

	Fecha=models.DateField(auto_now=True, verbose_name='Fecha')
	NombreAlumno=models.ForeignKey(Alumno,verbose_name='Alumno', on_delete=models.CASCADE)
	grado=models.ForeignKey(Grado, verbose_name='Grado', on_delete=models.CASCADE)	
	NombreMaestro=models.ForeignKey(Maestro, verbose_name='Maestro', on_delete=models.CASCADE, null=True)
	Descripcion=models.CharField(max_length=100, verbose_name='Descripción', blank=True)	

	def __str__(self):
			return'{}{}{}{}{}'.format(self.Fecha, self.NombreAlumno, self.grado, self.NombreMaestro, self.Descripcion)

	class Meta:
		verbose_name='Disciplina'
		verbose_name_plural='Disciplinas'