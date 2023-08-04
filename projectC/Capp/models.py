from django.db import models

# Create your models here.

class DadosGerais(models.Model):
    kic = models.IntegerField()
    Period = models.CharField(max_length=100)
    bjd0 = models.CharField(max_length=100)
    Period_td = models.CharField(max_length=100)
    e = models.CharField(max_length=100)
    a = models.CharField(max_length=100)
    omega = models.CharField(max_length=100)
    Aa = models.CharField(max_length=100)
    Bb = models.CharField(max_length=100)