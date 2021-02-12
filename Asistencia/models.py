from django.db import models

Estado_CHOICES=[
		('Escrito','Escrito'),
		('Llamada','Llamada'),
		('Ninguno','Ninguno'),
]

Nivel_CHOICES=[
		('Preprimario','Preprimario'),
		('Primario', 'Primario'),
		('Básico','Básico'),
		('Bachillerato','Bachillerato'),
		('PGA','PGA'),
]

Grado_CHOICES=[
		('Nursery','Nursery'),
		('Pre-Kinder','Pre-Kinder'),
		('Kinder','Kinder'),
		('Parvulos','Parvulos'),
		('Preprimaria','Preprimaria'),
		('Primero','Primero'),
		('Segundo','Segundo'),
		('Tercero','Tercero'),
		('Cuarto','Cuarto'),
		('Quinto', 'Quinto'),
		('Sexto', 'Sexto'),

]

Seccion_CHOICES=[
		('A','A'),
		('B','B'),
		('C','C'),
		('Única','Única'),

]


#class Nivel(models.Model):
	
#	Nivel=models.CharField(max_length=30, choices=Nivel_CHOICES, default='Primario', verbose_name='Nivel')	
	
#	def __str__(self):
#			return'{}'.format(self.Nivel)

#	class Meta:
#		verbose_name='Nivel'
#		verbose_name_plural='Nivel'




class Grado(models.Model):
	NombreGrado=models.CharField(max_length=30,choices=Grado_CHOICES, default='Primero', verbose_name='Grado')
	#Nivel=models.CharField(max_length=30, choices=Nivel_CHOICES, default='Primario', verbose_name='Nivel')	
	#eccion=models.CharField(max_length=30, verbose_name='Sección', choices=Seccion_CHOICES, default='A')
	
	def __str__(self):
			return'{}'.format(self.NombreGrado)

	class Meta:
		verbose_name='Grado'
		verbose_name_plural='Grados'

#class Seccion(models.Model):
#	Seccion=models.CharField(max_length=30, verbose_name='Sección', choices=Seccion_CHOICES, default='A')
	
#	def __str__(self):
#			return'{}'.format(self.Seccion)

	#class Meta:
	#	verbose_name='Seccipon'
	#	verbose_name_plural='Secciones'

class Alumno(models.Model):
	Nombres=models.CharField(max_length=80, verbose_name='Nombre Completo')
	

	def __str__(self):
			return'{}'.format(self.Nombres)

	class Meta:
		verbose_name='Alumno'
		verbose_name_plural='Alumnos'

class Maestro(models.Model):
	Nombres=models.CharField(max_length=80, verbose_name='Nombre Maestro')
	

	def __str__(self):
			return'{}'.format(self.Nombres)

	class Meta:
		verbose_name='Maestro'
		verbose_name_plural='Maestros'

class Asistencia(models.Model):

	Fecha=models.DateField(auto_now=True, verbose_name='Fecha')
	NombreAlumno=models.ForeignKey(Alumno, blank=True, null=True, verbose_name='Alumno', on_delete=models.CASCADE)
	grado=models.ForeignKey(Grado, verbose_name='Grado', on_delete=models.CASCADE)	
	NombreMaestro=models.ForeignKey(Maestro, verbose_name='Maestro', on_delete=models.CASCADE, null=True)
	TipoPermiso=models.CharField(max_length=15, choices=Estado_CHOICES, default='Ninguno', verbose_name='Tipo de Permiso')
	Descripcion=models.CharField(max_length=100, verbose_name='Descripción', blank=True)	

	def __str__(self):
			#return'{}'.format(self.Fecha)
			return'{}{}{}{}{}{}'.format(self.Fecha, self.NombreAlumno, self.grado, self.NombreMaestro, self.TipoPermiso, self.Descripcion)

	class Meta:
		verbose_name='Asistencia'
		verbose_name_plural='Asistencias'