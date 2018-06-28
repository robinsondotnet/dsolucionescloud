from veterinaria.Apps.GestionVeteriana.models import *
from django.contrib import admin

# Register your models here.

admin.site.register(Paciente)
admin.site.register(Especialidad)
admin.site.register(Veterinario)
admin.site.register(Sede)
admin.site.register(Diagnostico)