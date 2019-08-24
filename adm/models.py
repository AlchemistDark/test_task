from django.db import models

# Create your models here.

class urls_base(models.Model):
    url_name = models.CharField(max_length=1024)    # URL из списка
    flag1 = models.BooleanField()                   # обработано или ещё нет
    flag2 = models.BooleanField()                   # успешно или нет
    date_time = models.DateTimeField()              # дата и время обработки
    site_name = models.CharField(max_length=1024)   # заголовок страницы
    site_code = models.CharField(max_length=32)     # кодировка страницы
    h1_name = models.CharField(max_length=1024)     # заголовок H1
    
