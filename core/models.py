from django.db import models

class Trago(models.Model):
    nombre = models.CharField(max_length=100)
    preparacion = models.TextField()
    imagen = models.ImageField(upload_to='tragos/', blank=True, null=True)

    def __str__(self):
        return self.nombre




