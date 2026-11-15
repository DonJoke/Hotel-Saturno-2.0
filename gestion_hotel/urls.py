from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, HabitacionViewSet, ReservaViewSet

# default router crea todas las rutas  automáticamente sin tener que escribirlas una por una
router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'habitaciones', HabitacionViewSet)
router.register(r'reservas', ReservaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]