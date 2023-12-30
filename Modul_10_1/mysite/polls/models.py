from django.db import models

# Create your models here.
"""
Кожен клас в polls/models.py отримає своє представлення у базі даних. Атрибути цього класу стануть полями, а об'єкт 
класу — записом у таблиці.
Ми створили дві моделі для питань Question та для відповідей користувачів Choice.
"""


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
