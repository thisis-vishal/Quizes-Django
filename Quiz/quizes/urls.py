from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.welcome),
    path('quizzes',views.postQuiz.as_view()),
    path('quizzes/all',views.getQuizes.as_view()),
    path('quizzes/active',views.getActiveQuize.as_view()),
    path('quizzes/<postcode>',views.getQuiz.as_view()),
    path('quizzes/<postcode>/result',views.ansQuiz.as_view()),
    path('check/',views.checkStatus.as_view()),
]