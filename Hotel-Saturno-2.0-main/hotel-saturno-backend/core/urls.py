from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    # aqui conectamos todas las rutas que generó el router en la app
    path('api/', include('gestion_hotel.urls')), 
]
