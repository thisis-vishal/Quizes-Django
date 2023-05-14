from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('quizzes',views.postQuiz.as_view()),
    path('quizzes/<postcode>',views.getQuiz.as_view())
]