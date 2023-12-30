from django.urls import path

from . import views

"""
Ми визначаємо список urlpatterns, в якому будуть маршрути для нашого застосунку. Поки що тут тільки один маршрут під час 
звернення до застосунку polls і він оброблятиметься функцією index з файлу views.py. Цьому маршруту ми даємо ім'я index. 
Тепер кореневий каталог програми polls буде дозволений за допомогою views.index.
"""

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),      # /polls/1
    path('<int:question_id>/results/', views.results, name='results'),   # /polls/1/results
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
