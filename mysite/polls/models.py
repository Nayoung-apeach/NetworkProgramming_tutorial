import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date > timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # CASCADE 자동완성하면 생기는 소괄호 있으면 안된다.
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)  # ctrl + alt + l => 코드 포멧

    def __str__(self):
        return self.choice_text
