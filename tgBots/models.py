from statistics import mode
from django.db import models

# Create your models here.

class TableWorks(models.Model):

    id_user = models.CharField('ID заказа', max_length=50)
    works = models.CharField('Вид заказа', max_length=50)
    themes = models.CharField('Тема заказа', max_length=250)
    days = models.CharField('Срок выполнения заказа', max_length=50)
    origins = models.CharField('Оригинальность работы', max_length=50)
    plus_func = models.TextField('Дополнительная информация')
    url_name = models.CharField('Ссылка на скачивание', max_length=50,null=True)
    
    
    def __str__(self):
        workss = self.works
        themes = self.themes
        days = self.days
        origins = self.origins
        plus_func = self.plus_func
        url_name = self.url_name
        return f'{workss} {themes} {days} {origins} {plus_func} {url_name}'
   
