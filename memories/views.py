from django.shortcuts import render
from .models import Memory

memories = [
    {
        'id': 1, 'title': 'testing123', 'date': 12, 
        'description': 'bruh i hate this'
    },
    {
        'id': 2, 'title': 'blahblah', 'date': 444, 
        'description': 'fuck this shit'
    }
]

def index(request):
    template_data = {}
    template_data['title'] = 'Memories'
    template_data['memories'] = Memory.objects.all
    return render(request, 'memories/index.html',
                  {'template_data': template_data})

def show(request, id):
    memory = Memory.objects.get(id=id)
    template_data = {}
    template_data['title'] = memory.title
    template_data['memory'] = memory
    return render(request, 'memories/show.html',
                  {'template_data' : template_data})

#this is a comment for github purposes