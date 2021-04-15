# import datetime
#
# from django.db import models
# from django.utils import timezone
#
#
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#     def was_published_recently(self):
#         return self.pub_date > timezone.now() - datetime.timedelta(days=1)
#
#     def __str__(self):
#         return self.question_text
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)  # CASCADE 자동완성하면 생기는 소괄호 있으면 안된다.
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)  # ctrl + alt + l => 코드 포멧
#
#     def __str__(self):
#         return self.choice_text

import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def was_published_recently(self):
        now = timezone.now()
        return now >= self.pub_date >= now - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolen = True
    was_published_recently.short_description = 'Published recently?'

    # 그날그날 최신 글
    def was_published_recently(self):
        now= timezone.now()
        return now >= self.pub_date >= now - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

# 1. models.py 변경하기
# 2. makemigrations 를 통해 변경사항에 대한 마이그레이션을 만들기
# 3. migrate 를 통해 변경사항을 데이터베이스에 적용하기