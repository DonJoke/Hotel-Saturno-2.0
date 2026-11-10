from rest_framework import serializers 
from .models import cliente, habitacion, reserva
from django.core.exceptions import ValidationError as DjangoValidationError
#aca haremos las serializasiones pa trasnforamar estos en JSON SHH

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = cliente
        fields = '__all__'

class HabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = habitacion
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = reserva
        fields = '__all__'

    
    def validate(self, attrs):
        instancia = reserva(**attrs)
        try:
            instancia.clean()
        except DjangoValidationError as e:
            raise serializers.ValidationError(e.message_dict if hasattr(e, 'message_dict') else list(e.messages))
        
        return attrs