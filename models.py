from django.db import models

# Create your models here.

# Modelo para el dueño

class Dueño(models.Model):
    idDueño = models.IntegerField(primary_key=True, verbose_name='Id del dueño')
    nombreDueño = models.CharField(max_length=50, verbose_name='Nombre del dueño')

    def __str__(self):
        return self.nombreDueño

# Modelo para la mascota

class Mascota(models.Model):
    idMascota = models.IntegerField(primary_key=True, verbose_name='Id de la mascota')
    nombreMascota = models.CharField(max_length=20, verbose_name='Nombre de la mascota')
    especieMascota = models.CharField(max_length=20, null = True, blank = True, verbose_name='Especie de la mascota')
    razaMascota = models.CharField(max_length=20, null = True, blank = True, verbose_name='Raza de la mascota')
    numeroContacto = models.CharField(max_length=11, verbose_name='Numero de contacto')
    dueño = models.ForeignKey(Dueño, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreMascota

# Modelo para la ficha

class Ficha(models.Model):
    idFicha = models.IntegerField(primary_key=True, verbose_name='Id de la ficha')
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)

    def __int__(self):
        return self.idFicha
