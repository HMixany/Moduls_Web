"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

    Щоб зареєструвати сам застосунок polls, у проекті потрібно модифікувати mysite/urls.py:
"""
# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
"""
Тут вже є шлях до адмін-панелі нашого проекту — admin/, і ми додали шлях до створеного застосунку: polls/. 
Функція include потрібна, щоб повідомити Django, що всі маршрути, що починаються з polls/, повинні оброблятися 
застосунком polls. Сам маршрут втрачає префікс polls (відбудеться заміна polls/ на /) і відправляється для обробки вже 
в сам застосунок.

Щоб переглянути результат роботи нашого застосунку, можна виконати python manage.py runserver та перейти на 
http://localhost:8000/polls/
"""