from django.db import models

class WithVariation(models.Model):
    kic = models.IntegerField()
    Period = models.CharField(max_length=100)
    epoch = models.CharField(max_length=100)
    Period_td = models.CharField(max_length=100)
    epoch_td = models.CharField(max_length=100)
    e = models.CharField(max_length=100)
    a = models.CharField(max_length=100)
    omega = models.CharField(max_length=100)
    Aa = models.CharField(max_length=100)
    Bb = models.CharField(max_length=100)

    def __str__(self):
        return str(self.kic)

class OutVariation(models.Model):
    kic = models.IntegerField()
    Period = models.CharField(max_length=100)
    epoch = models.CharField(max_length=100)

    def __str__(self):
        return str(self.kic)
