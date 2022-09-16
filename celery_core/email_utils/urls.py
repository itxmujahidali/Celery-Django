from django.contrib import admin
from django.urls import path
from .views import celery_task
from . import views

urlpatterns = [
    path('celery/', views.celery_task, name="celery-task")
]
