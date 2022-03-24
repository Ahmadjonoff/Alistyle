from django.db import models
from userapp.models import *
from asosiy.models import *

class Tanlangan(models.Model):
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)

class Savat(models.Model):
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    son = models.PositiveSmallIntegerField(default=1)

class Buyurtma(models.Model):
    savat = models.ManyToManyField(Savat)
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    sana = models.DateField(auto_now_add=True)
    yetkazish_puli = models.IntegerField()
    summa = models.IntegerField()
    status = models.CharField(max_length=15, default='Jarayonda')