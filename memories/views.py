from django.shortcuts import render, redirect
from .models import Memory
from django.contrib.auth.decorators import login_required

def index(request):
    template_data = {'title': 'Memories'}
    if request.user.is_authenticated:
        user_memories = Memory.objects.filter(owner=request.user)
        show_public = request.GET.get('public') == '1'
        public_memories = Memory.objects.filter(is_public=True).exclude(owner=request.user) if show_public else []
        template_data['memories'] = list(user_memories) + list(public_memories)
        template_data['show_public'] = show_public
    else:
        template_data['memories'] = Memory.objects.filter(is_public=True)
        template_data['show_public'] = True
    return render(request, 'memories/index.html', {'template_data': template_data})


def show(request, id):
    memory = Memory.objects.get(id=id)
    template_data = {}
    template_data['title'] = memory.title
    template_data['memory'] = memory
    return render(request, 'memories/show.html',
                  {'template_data' : template_data})

@login_required
def create_memory(request):
    if request.method == 'POST' and request.POST['title'] != '' and request.POST['date'] != '' and request.POST['description'] != '':
        memory = Memory()
        memory.title = request.POST['title']
        memory.date = request.POST['date']
        memory.description = request.POST['description']
        memory.owner = request.user

        if request.user.business:
            memory.is_public = True
            memory.business_label = request.user.username
        else:
            memory.is_public = False
            memory.business_label = ""

        # Handle image upload
        if 'image' in request.FILES:
            memory.image = request.FILES['image']

        memory.save()
        return redirect('memories')
    else:
        return redirect('memories')
