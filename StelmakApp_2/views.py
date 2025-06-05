from django.shortcuts import render
import datetime,math
from django.http import HttpResponse
from django.shortcuts import render, redirect
from collections import defaultdict
from django.urls import resolve
from .models import about_programm

def index(request):
    return render(request, "StelmakApp_2/index.html")

def about_me(request):
    me = [    {       
        'name': 'Еремеева Анна Владимировна',
        'img': 'images/me1.jpg',
        'email': 'averemeeva@edu.hse.ru',
        'phone': '+79060843298',
        'resume': 'Студентка 3 курса ОП "Социология". Имею богатый опыт проведения академических исследований, публикаций статей в журналах и участия в научных конференциях. Обладаю навыками написания академических текстов. Интересуюсь академическими и коммерческими исследованиями, в особенности UX исследованиями.'
    }
    ] 

    dict_of_array = {'me': me}
    context = {'dict_of_array': dict_of_array}
    return render(request, 'StelmakApp_2/about_me.html', context)

def about_uni (request):
    return render(request, 'StelmakApp_2/about_uni.html')

def about_managment(request):
    info = [
    {
        'name': 'Симонова Ольга Александровна',
        'job' : 'Руководитель программы',
        'img': 'images/manager.jpg',
        'email': 'osiminiva@hse.ru'
    },
    {
        'name': 'Козин Виктор Ярославович',
        'job' : 'Менеджер программы',
        'img': 'images/supervisor.png',
        'email': 'vkozin@hse.ru'
    },
    ]
    dict_of_array = {'info': info}
    context = {'dict_of_array': dict_of_array}
    return render(request, 'StelmakApp_2/about_managment.html', context)

def about_friends(request):
    info_classmates = [    
    {'name': 'Петров Николай Петрович', 'img': 'images/nick.jpg', 'email': 'nppetrov@edu.hse.ru'},
    {'name': 'Богданова Евгения Васильевна', 'img': 'images/zhenya.jpg', 'email': 'evbogdanova@edu.hse.ru'}
    ]
    dict_of_array = {'info_classmates': info_classmates}
    context = {'dict_of_array': dict_of_array}
    return render(request, 'StelmakApp_2/about_friends.html', context)


def nav_view(request):
    nav_items = [
        {'name': 'Главная', 'url': 'StelmakApp:index', 'category': 'basic'},
        {'name': 'Я', 'url': 'StelmakApp_2:about_me', 'category': 'profile'},
        {'name': 'Описание моей образовательной программы', 'url': 'StelmakApp_2:about_uni', 'category': 'edu'},
        {'name': 'Менеджмент', 'url': 'StelmakApp_2:about_managment', 'category': 'edu'},
        {'name': 'Сокурсники', 'url': 'StelmakApp_2:about_friends', 'category': 'social'},
    ]
    filter_cat = request.GET.get('filter')
    if filter_cat:
        nav_items = [item for item in nav_items if item['category'] == filter_cat]
    return render(request, 'your_template.html', {'nav_items': nav_items})

def navigation_view(request):
    nav_items = [
        {'name': 'Главная', 'url': 'StelmakApp:index', 'group': 'Основное'},
        {'name': 'Я', 'url': 'StelmakApp_2:about_me', 'group': 'Обо мне'},
        {'name': 'Описание моей образовательной программы', 'url': 'StelmakApp_2:about_uni', 'group': 'Образование'},
        {'name': 'Менеджмент', 'url': 'StelmakApp_2:about_managment', 'group': 'Образование'},
        {'name': 'Сокурсники', 'url': 'StelmakApp_2:about_friends', 'group': 'Сообщество'},
    ]

    grouped = defaultdict(list)
    for item in nav_items:
        grouped[item['group']].append(item)

    grouped_sorted = dict(sorted(grouped.items()))
    for group, items in grouped_sorted.items():
        grouped_sorted[group] = sorted(items, key=lambda x: x['name'])

    current_url_name = resolve(request.path_info).url_name

    return render(request, 'navigation_template.html', {
        'grouped_nav': grouped_sorted,
        'current_url_name': current_url_name,
    })

def about_programm_read(request):
    all_obj = about_programm.objects.order_by('text')
    return render(request, 'StelmakApp_2/about_programm_read.html', {'all_obj': all_obj})