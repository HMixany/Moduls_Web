from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader

from .models import Question

# Create your views here.


# @login_required
def index(request):
    question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'question_list': question_list}
    return render(request, 'polls/index.html', context)
    # template = loader.get_template('polls/index.html')
    # rendered_template = template.render(context, request)
    # return HttpResponse(rendered_template)
    # output = ', '.join([q.question_text for q in question_list])
    # return HttpResponse(output)
    # return HttpResponse("Hello, world. You're at the polls index.")


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'polls/detail.html', context)
    # return HttpResponse(f'Detail for question # {question_id}')


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'polls/results.html', context)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choice = question.choice_set.get(pk=request.POST["choice"])
    choice.votes += 1
    choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
