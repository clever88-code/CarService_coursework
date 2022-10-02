from turtle import title
from django.db import models

# Create your models here.


class Articles(models.Model):
    title = models.CharField('название', max_length=50)
    text_news = models.CharField('статья', max_length=50)
    date = models.DateTimeField('Дата побликации')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'новость'
        #название таблице в множественном числе
        verbose_name_plural = 'новости'
    
