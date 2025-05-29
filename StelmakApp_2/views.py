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
        'name': 'Стельмак Елизавета Алексеевна',
        'img': 'images/me.jpg',
        'email': 'eastelmak@edu.hse.ru',
        'phone': '+79643728037',
        'resume': 'Студентка 3 курса филологического факультета, специализация — русский язык и литература. Обладаю хорошими навыками аналитического чтения, редактирования текстов и написания научных работ. Имею опыт ведения учебных проектов, участия в конференциях и литературных конкурсах. Интересуюсь редакторской и переводческой деятельностью, а также преподаванием.'
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
        'name': 'Шерстинова Татьяна Юрьевна',
        'job' : 'Руководитель программы',
        'img': 'images/Sherstinova.jpg',
        'email': 'tusherstinova@edu.hse.ru'
    },
    {
        'name': 'Чумакова Елена Вадимовна',
        'job' : 'Менеджер программы',
        'img': 'images/Chumakova.jpg',
        'email': 'evchumakova@edu.hse.ru'
    }, 
    ]
    dict_of_array = {'info': info}
    context = {'dict_of_array': dict_of_array}
    return render(request, 'StelmakApp_2/about_managment.html', context)

def about_friends(request):
    info_classmates = [    
    {'name': 'Мозоль Игорь Николаевич', 'img': 'images/Mozol.jpg', 'email': 'inmozol@edu.hse.ru'},
    {'name': 'Завсегдалина Екатерина Иванова', 'img': 'images/Zavsegdalina.jpg', 'email': 'eizavsegdalina@edu.hse.ru'}
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