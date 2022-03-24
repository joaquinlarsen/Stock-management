from django.db import models

# Create your models here.


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    presentacion = models.CharField(max_length=50)
    tipo_bebida = models.CharField(max_length=50)
    id_interno = models.CharField(max_length=100, primary_key=True)
    precio = models.FloatField()
    cantidad_stock = models.PositiveIntegerField()
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.tipo_bebida} {self.nombre} {self.presentacion}"
