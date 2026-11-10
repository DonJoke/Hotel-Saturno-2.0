#HERRAMIENTAS DJANGO#
from django.db import models
from django.core.exceptions import ValidationError

#vamos a tener 3 modelos,cliente,habitacion y reserva :D 
#proximamente vamos a implementar un import "from rut_validator import validate_rut" que valida rut
#solo numeros,con puntos y guion,sin puntos y guion pero que se activa mediante un pip mediante la shell.
#-----------------------------------------------------------------------------------------------------------------------------------------
#METODO VALIDAR RUT#
def validar_rut(value):
   # aca se busca es limpiar o transformar el rut en uno sin puntos
   # o guiones y transformar todo a mayusculas para evaluarlo sin problemas. 
    rut_limpio = value.upper().replace(".", "").replace("-", "")
    
    if len(rut_limpio) < 2:
        raise ValidationError("El RUT ingresado es demasiado corto.")
    aux = rut_limpio[:-1]   # auxiliar sera el cuerpo del rut
    dv = rut_limpio[-1]     # dv sera dígito verificador
    #lo que buscamos en esta logica es separar el rut en 2 partes entre el cuerpo y el numero verificador,
    #si el rut no esta en ese orden al momento de escribirlo apercera el error "el rut es demasiado corto"
    
    
    # otro problema,al momento de ingresar rut es escribir cualquier cosa,
    # con el siguiente comando si el usuario no entrega un formato rut aparecera otro 
    # error que dira soolamente debe contener numeros esceptuando el dijito verificador 
    if not aux.isdigit():
        raise ValidationError("El cuerpo del RUT debe contener únicamente números.")
        
    #otro error que se manejo es el del dijito verificador,en esta parte si dv(dijito verificador)
    #no es un numero o una k aparecera otro error
    if not (dv.isdigit() or dv == 'K'):
        raise ValidationError("El dígito verificador debe ser un número del 0 al 9 o la letra K.")

    #-----------------------------------------------------------------------------------------------------------------------------------    
    #APLICACION MODELO 11 CHILENSI LOGIC# 
    suma = 0
    factor = 2
    #empieza la suma y la multipliccion de 2 en hacia adelante
    for r in reversed(aux):#se da vuelta el cuerpo del rut
        suma += int(r) * factor
        factor += 1
        if factor > 7:#si el factor llega hasta el 7 se reinicia y empieza por el 2 otra vez
            factor = 2
            #cada numero del cuerpo dado vuelta s emultiplica uno por uno desde el 2 en hacia adelante
    res = 11 - (suma % 11)
    if res == 11:
        dv_esperado = '0'
    elif res == 10:
        dv_esperado = 'K'
    else:
        dv_esperado = str(res)#se obtiene el residuo de la suma divido en 11 y se le resta 11 para obtener el supuesto numero verificador
        
    #finalmente esta parte compara el digito ingresado con el que dio anteriormente y comprueba si es valido.
    if dv_esperado != dv:
        raise ValidationError(f"El RUT '{value}' no es válido (el dígito verificador es incorrecto).")
#---------------------------------------------------------------------------------------------------------------------------------------------
#MODELOS CREADOS#
class cliente(models.Model):
    nombre = models.CharField(max_length=100)
    # Aplicamos la función validadar_rut al campo RUT
    rut = models.CharField(max_length=12, unique=True, validators=[validar_rut])
    telefono = models.CharField(max_length=15)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} ({self.rut})"


class habitacion(models.Model):
    numero_habitacion = models.CharField(max_length=10, unique=True)
    piso = models.IntegerField()
    tipo_de_habitacion = models.CharField(max_length=50) #la simple doble o la suittt cpor ejemplox
    precio_noche = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Habitación {self.numero_habitacion} - {self.tipo_de_habitacion}"

class reserva(models.Model):
  
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE, related_name='reservas')#multiples reservas pueden ser de un cliente
    habitacion = models.ForeignKey(habitacion, on_delete=models.CASCADE, related_name='reservas')#una habitacion puede tener muchas reservas.
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=20, default='Confirmada')
#------------------------------------------------------------------------------------------------------------------------------------------------
#METODOS Y ERRORES DE RESERVA#
    def clean(self):
        super().clean()
        #aca con este metodo nos aparece el siguiente error:que si la fecha de inicio es mayor entonces falla.
        if self.fecha_inicio and self.fecha_fin:
            if self.fecha_inicio >= self.fecha_fin:
                raise ValidationError("La fecha de inicio debe ser anterior a la fecha de fin.")
            
            #evitamos quue hayan reservas el mismo dia.
            reservas_existentes = reserva.objects.filter(habitacion=self.habitacion)
            if self.pk:
                reservas_existentes = reservas_existentes.exclude(pk=self.pk)
            for r in reservas_existentes:
                if (self.fecha_inicio < r.fecha_fin) and (self.fecha_fin > r.fecha_inicio):
                    raise ValidationError(
                        f"La habitación {self.habitacion.numero_habitacion} ya se encuentra reservada del {r.fecha_inicio} al {r.fecha_fin}."
                    )
#guarda los datos, no sin usar un clean antes y verificar si no se cumple algun errror que pusimos osino nos lanza 
# errrror si esta todo bien nos lanza la reserva en la bd corte reserva#1 lepepe almonacid(hab.67)
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Reserva #{self.id} - {self.cliente.nombre} (Hab. {self.habitacion.numero_habitacion})"