from django.shortcuts import render

# Create your views here.
from django.http.response import HttpResponse
from .task import sender_func

def celery_task(request):
    sender_func.delay()
    return HttpResponse("Email Has Been Sent")