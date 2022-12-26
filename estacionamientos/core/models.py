from django.db import models
import uuid



class Cliente(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=30)
    patente_vehiculo =models.CharField(max_length=30)
    hora_ingreso = models.TimeField(auto_now=False, auto_now_add=False)
    hora_salida = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.nombre


class Tipovehiculo(models.Model):
    id = models.UUIDField (primary_key=True,default=uuid.uuid4, editable=False)
    tipo_segmento = models.CharField (max_length=30)

    def __str__(self):
        return self.tipo_segmento

class Estado(models.Model):
    id = models.UUIDField (primary_key=True, default=uuid.uuid4, editable=False)
    estado = models.CharField (max_length=30)

    def __str__(self):
        return self.estado

class Nivel_estacionamiento(models.Model):
    id = models.UUIDField (primary_key=True,default=uuid.uuid4, editable=False)
    nivel = models.CharField(max_length=10)
    

    def __str__(self):
        return self.nivel


class Calzo(models.Model):
    id = models.UUIDField (default=uuid.uuid4, editable=False)
    numero_estacionamiento = models.PositiveIntegerField(primary_key=True)
    tipo_vehiculo = models.ManyToManyField (Tipovehiculo)
    estado = models.ForeignKey(Estado,on_delete=models.CASCADE,null=True,blank=True)
    cliente = models.ForeignKey(Cliente ,on_delete=models.CASCADE,null=True,blank=True)
    nivel_estacionamiento = models.ForeignKey(Nivel_estacionamiento ,on_delete=models.CASCADE,null=True,blank=True)


    def __str__(self):
        return self.numero_estacionamiento

