from django.db import models

# Create your models here.
from django.db import models

class Jurisprudencia(models.Model):
    tipoCausa = models.CharField(max_length=100, default='')
    rol = models.CharField(max_length=100, default='')
    caratula = models.CharField(max_length=100, default='')
    nombreProyecto = models.CharField(max_length=100, default='')
    fechaSentencia = models.DateField(default="2023-10-25")
    descriptores = models.CharField(max_length=100, default='')
    linkSentencia = models.CharField(max_length=100, default='')
    urlSentencia = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.tipoCausa
