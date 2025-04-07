from django.shortcuts import render, redirect
from .models import Memory
from django.contrib.auth.decorators import login_required

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

#@login_required
def create_memory(request):
    if request.method == 'POST' and request.POST['title']!= '' and request.POST['date']!= '' and request.POST['description']!= '':
        memory = Memory()
        memory.title = request.POST['title']
        #memory.user = request.user
        memory.date = request.POST['date']
        memory.description = request.POST['description']
        memory.save()
        return redirect('memories')
    else:
        return redirect('memories')