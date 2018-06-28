from django.db import models

# Create your models here.

from django.db import models

class Paciente(models.Model):

	especie = models.CharField(max_length=50)

	animal = models.CharField(max_length=50)

	nombre = models.CharField(max_length=50)

	fecha_Adopcion = models.DateField()

	SEXOS = ( ('F','Femenino'), ('M','Masculino') )

	sexo = models.CharField(max_length=1, choices=SEXOS, default='M')

	def NombreCompleto(self):	

		cadena = "{0} - {1} - {2}"	

		return cadena.format(self.especie, self.animal, self.nombre)

	def __str__(self):

		return self.NombreCompleto()

class Especialidad(models.Model):

	nombre_esp = models.CharField(max_length=100)

	descripcion = models.CharField(max_length=80)

	def __str__(self):

		return self.nombre_esp

class Veterinario(models.Model):

	paterno = models.CharField(max_length=50)

	materno = models.CharField(max_length=50)

	nombre_vet = models.CharField(max_length=50)

	especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)

	def NombreCompleto(self):

		cadena = "{0} {1} {2}"

		return cadena.format(self.paterno, self.materno, self.nombre_vet)

	def __str__(self):

		return self.NombreCompleto()

class Sede(models.Model):

	veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE)

	ubicacion = models.CharField(max_length=50)

	def __str__(self):

		return self.ubicacion

class Diagnostico(models.Model):

	paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

	veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE)

	fecha_diag = models.DateField()

	diag = models.CharField(max_length=80)

	monto = models.DecimalField(max_digits=6,decimal_places=2)

	def NombreCompleto(self):

		cadena = "{0} {1} {2}"

		return cadena.format(self.fecha_diag, self.diag, self.monto)
		
	def __str__(self):

		return self.NombreCompleto()