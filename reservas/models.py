from django.db import models

# Create your models here.
# RESERVADO, COMPLETADA, ANULADA, NO ASISTEN

estado = [
    ('reservado','RESERVADO'),
    ('realizado','REALIZADO'),
    ('anulada','ANULADA'),
    ('no asiste','NO ASISTE')
]


class Reserva(models.Model):
    rut = models.CharField(max_length=12)  
    nombre = models.CharField(max_length = 50)
    fecha_reserva = models.DateField()
    telefono= models.IntegerField()
    cantidad_personas = models.IntegerField()
    hora  = models.TimeField()
    observacion = models.TextField(blank=True)
    estado_reserva = models.CharField(max_length = 35,choices = estado)






