from django.db import models

class about_programm(models.Model):
    title = models.CharField('Название', max_length = 50)
    text = models.TextField('Текст')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "О_программе_Таблица"
        verbose_name_plural = "О_программе_Таблицы"
        ordering = ("-pk", )

# Create your models here.
