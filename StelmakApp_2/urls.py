from django.urls import path
from . import views

app_name = 'StelmakApp_2'

urlpatterns = [
    path('', views.index, name='index'),
    path('about_me/', views.about_me, name='about_me'),
    path('about_uni/', views.about_uni, name='about_uni'),
    path('about_management', views.about_managment, name='about_managment'),
    path('about_friends', views.about_friends, name='about_friends'),
    path('about_programm_read', views.about_programm_read, name='about_programm_read')
]