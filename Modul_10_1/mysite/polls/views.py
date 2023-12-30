from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
#
#
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# from django.http import HttpResponse
#
# from .models import Question
#
#
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)


"""
Тепер застосунок polls відображає клієнту останні 5 питань при запиті на кореневий ресурс застосунку /
Але самі дані в базі даних поки що відсутні, і щоб їх додати туди, потрібна адмін-панель
"""

# from django.http import HttpResponse
# from django.template import loader
#
# from .models import Question
#
#
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse

from .models import Question, Choice


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


"""
Об'єкт request містить атрибут POST, який поводиться як словник, і ви можете отримати значення полів форми: 
request.POST['choice']. Оновлення значення поля виконує метод choice_set, цей метод автоматично створений Django і 
встановлює зв'язок між Question і Choice об'єктами.

Після оновлення інформації в базі ми можемо надіслати redirect відповідь, щоб браузер автоматично перенаправив 
користувача на іншу сторінку. Для цього використовується HttpResponseRedirect, який перенаправить на URL, що відповідає 
за відображення результатів polls:results з аргументом у запиті, що дорівнює question.id. Щоб згенерувати цю URL-адресу, 
викликаємо функцію reverse
"""


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
