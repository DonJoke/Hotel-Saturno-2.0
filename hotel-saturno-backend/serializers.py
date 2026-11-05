from rest_framework import serializers 
from .models import cliente, habitacion, reserva
from django.core.exceptions import ValidationError as DjangoValidationError
#aca haremos las serializasiones pa trasnforamar estos en JSON SHH