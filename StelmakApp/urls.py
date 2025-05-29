from django.urls import path
from . import views
from django.contrib import admin

app_name = 'StelmakApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('programm_model_form/', views.programm_model_form, name='programm_model_form'),
    path('programm_result/', views.programm_result, name='programm_result'),
    path('table/', views.table, name='table'),
    path('datetimenow/', views.datetimenow, name='datetimenow'),
    path('admin/', admin.site.urls),
    path('programm_form/', views.programm_form, name='programm_form')
]

