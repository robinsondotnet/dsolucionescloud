from django.shortcuts import render
from django.http import HttpResponse
import datetime
from veterinaria.Apps.GestionVeteriana.models import *
# Create your views here.

def lista_paciente(request): 
	obj = Paciente.objects.all() 
	for abc in obj: 
		obj_especie = abc.especie 
		obj_animal = abc.animal 
		obj_nombre = abc.nombre
		obj_fecha_Adopcion = abc.fecha_Adopcion
		obj_sexo = abc.sexo
	context = { 
		"obj":obj, 
		"obj_especie":obj_especie, 
		"obj_animal":obj_animal, 
		"obj_nombre":obj_nombre, 
		"obj_fecha_Adopcion":obj_fecha_Adopcion,
		"obj_sexo":obj_sexo,
	} 
	return render(request,"lista_paciente.html",context)
#A partir de acá puede haber error:
def lista_veterinario(request):
	obj = Veterinario.objects.all() 
	for abc in obj: 
		obj_paterno = abc.paterno 
		obj_materno = abc.materno 
		obj_nombre_vet = abc.nombre_vet
		obj_especialidad = abc.especialidad
	context = { 
		"obj":obj, 
		"obj_paterno":obj_paterno, 
		"obj_materno":obj_materno, 
		"obj_nombre_vet":obj_nombre_vet, 
		"obj_especialidad":obj_especialidad,
	} 
	return render(request,"lista_veterinario.html",context)

def lista_sede(request):
	obj = Sede.objects.all() 
	for abc in obj: 
		obj_veterinario = abc.veterinario 
		obj_ubicacion = abc.ubicacion
	context = { 
		"obj":obj, 
		"obj_veterinario":obj_veterinario, 
		"obj_ubicacion":obj_ubicacion,
	} 
	return render(request,"lista_sede.html",context)
	
def contacto(request):
	return render(request,"contactenos.html",context)