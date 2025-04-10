from django.shortcuts import render
from django.http import HttpResponse

def accounts(request):
    return HttpResponse("Hello world!")