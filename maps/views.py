from django.shortcuts import render
from django.http import HttpResponse

def maps(request):
    return render(request, "maps.html")
