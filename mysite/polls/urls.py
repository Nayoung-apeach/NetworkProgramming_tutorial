from django.urls import path

from mysite.polls import views

urlpatterns = [
    path('', views.index, name='index'),
]