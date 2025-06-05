from django.db import models

# import datetime

courses_choices = (
    (1, 'первый'),
    (2, "второй"),
    (3, "третий"),
    (4, "четвёртый"),
)


class Educational_ProgrammModel(models.Model): #столбцы в таблице
    name = models.CharField(
        verbose_name="ФИО",
        default='Смирнов Иван Иванов',
        max_length=500,
    )
    date_of_birth = models.DateField(
        verbose_name="Дата рождения", #здесь можно изменить формат на дату,
        default='2004-05-10',

    )
    year = models.IntegerField(
        verbose_name="Год поступления", default=2022
    )
    courses = models.IntegerField(
        verbose_name="Курс",
        choices=courses_choices,
        default=3,
        help_text='от 1 до 4'
    )
    last_year = models.IntegerField(
        verbose_name="Год выпуска",
        default=2026,
        max_length=255,
    )
    result = models.IntegerField(
        verbose_name="Сколько осталось учиться",
        default=4,
        max_length=255,
    )
    current_date = models.DateTimeField(
        verbose_name="Дата изменения(save)", auto_now=True
    )

    def __str__(self):
        # return self.task
        # return '%s %s' % (self.task, self.current_date)
        return f"self.id:{self.id}; self.task:{self.name}"

    class Meta:
        verbose_name = "Я_и_программа_Таблица"
        verbose_name_plural = "Я_и_программа_Таблицы"
        ordering = ("-pk", )


# current_date = models.DateTimeField("ДатаВремя", default=datetime.datetime.now())
# current_date = models.DateTimeField("ДатаВремя", auto_now_add=True)

# python manage.py makemigrations
# python manage.py migrate

# admin.py
# from django.contrib import admin
# # Register your models here.
# from .models import Abc
# admin.site.register(Abc)


# forms.py
# from django.forms import ModelForm
# from .models import Abc
#
# class CreateAbcForm(ModelForm):
#     class Meta:
#         model = Abc
#         fields = ['task', 'a' ,'b' ,'c', 'c_calc']