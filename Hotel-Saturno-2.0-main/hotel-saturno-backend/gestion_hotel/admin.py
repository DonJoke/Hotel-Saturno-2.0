from django.contrib import admin
from .models import cliente, habitacion, reserva

# Registramos los modelos para que aparezcan en el panel de administración
admin.site.register(cliente)
admin.site.register(habitacion)
admin.site.register(reserva)