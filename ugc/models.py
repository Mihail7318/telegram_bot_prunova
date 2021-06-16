from django.db import models


# Create your models here.


class pars(models.Model):
    title = models.CharField("Название пары", max_length=25)

    teacher = models.CharField(max_length=250)
    room = models.CharField(max_length=25)


class shedule(models.Model):
    dn = models.CharField("День недели", max_length=25)
    group = models.CharField("Группа", max_length=25)
    date = models.DateField("Дата")
    par = models.ManyToManyField(pars)
