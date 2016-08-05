from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class tipo_cambio(models.Model):
    tipo_cambio = models.CharField(max_length=10)
    mes = models.CharField(max_length=20)
    fecha = models.DateField(auto_now=True)    