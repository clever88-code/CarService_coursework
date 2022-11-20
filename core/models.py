from django.db import models

class Firms(models.Model):
    name_firms = models.CharField('Названия фирмы автомобиля', max_length=60)

    class Meta:
        verbose_name = 'Фирма автомобиля'
        verbose_name_plural = 'Фирмы автомобилей'

class CarMarks(models.Model):
    firms = models.ForeignKey(Firms, on_delete=models.RESTRICT)
    name_car_marks = models.CharField('Названия марки автомобиля',max_length=30)

    class Meta:
        verbose_name = 'Марка автомобиля'
        verbose_name_plural = 'Марки автомобилей'


class Cars(models.Model):
    carmarks = models.ForeignKey(CarMarks, on_delete=models.RESTRICT)
    car_number = models.CharField('Названия номера автомобиля',max_length=15)

    class Meta:
        verbose_name = 'Номер автомобиля'
        verbose_name_plural = 'Номера автомобилей'
