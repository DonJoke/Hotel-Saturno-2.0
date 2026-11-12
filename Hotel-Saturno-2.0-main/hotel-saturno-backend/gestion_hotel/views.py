from rest_framework import viewsets
from .models import cliente, habitacion, reserva
from .serializers import ClienteSerializer, HabitacionSerializer, ReservaSerializer

# ViewSet para Cliente
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = cliente.objects.all()
    serializer_class = ClienteSerializer

# ViewSet para Habitación
class HabitacionViewSet(viewsets.ModelViewSet):
    queryset = habitacion.objects.all()
    serializer_class = HabitacionSerializer

# ViewSet para Reserva
class ReservaViewSet(viewsets.ModelViewSet):
    queryset = reserva.objects.all()
    serializer_class = ReservaSerializer