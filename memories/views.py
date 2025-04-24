from django.shortcuts import render, redirect, get_object_or_404
from .models import Memory
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse

def index(request):
    template_data = {'title': 'Memories'}
    if request.user.is_authenticated:
        user_memories = Memory.objects.filter(owner=request.user)
        show_public = request.GET.get('public', '1') == '1'
        public_memories = Memory.objects.filter(is_public=True).exclude(owner=request.user) if show_public else []
        template_data['memories'] = list(user_memories) + list(public_memories)
        template_data['show_public'] = show_public
    else:
        template_data['memories'] = Memory.objects.filter(is_public=True)
        template_data['show_public'] = True
    return render(request, 'memories/index.html', {'template_data': template_data})


def show(request, id):
    memory = get_object_or_404(Memory, id=id)
    template_data = {}
    template_data['title'] = memory.title
    template_data['memory'] = memory
    return render(request, 'memories/show.html',
                  {'template_data' : template_data})

def memory_locations(request):
    memories = Memory.objects.filter(Q(is_public=True) | Q(owner=request.user)) 
    data = [
        {
            'lat': memory.latitude,
            'lng': memory.longitude,
            'title': memory.title,
            'description': memory.description,
            'date': memory.date.strftime("%B %d, %Y"),
            'image_url': memory.image.url if memory.image else None,
            'business_label': memory.business_label,
            'is_owner': memory.owner == request.user
        }
        for memory in memories
    ]
    return JsonResponse(data, safe=False)

@login_required
def create_memory(request):
    if request.method == 'POST' and request.POST['title'] != '' and request.POST['date'] != '' and request.POST['description'] != '':
        memory = Memory()
        memory.title = request.POST['title']
        memory.date = request.POST['date']
        memory.latitude = request.POST.get('latitude', 0.0)
        memory.longitude = request.POST.get('longitude', 0.0)
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
    
@login_required
def edit(request, id):
    memory = get_object_or_404(Memory, id=id, owner=request.user)
    
    if request.method == 'POST':
        memory.title = request.POST['title']
        memory.date = request.POST['date']
        memory.description = request.POST['description']
        memory.latitude = request.POST.get('latitude', 0.0)
        memory.longitude = request.POST.get('longitude', 0.0)
        
        # Handle image update
        if 'image' in request.FILES:
            memory.image = request.FILES['image']
        
        memory.save()
        return redirect('memories.show', id=memory.id)
    
    template_data = {
        'title': f"Edit {memory.title}",
        'memory': memory
    }
    return render(request, 'memories/edit.html', {'template_data': template_data})
    
@login_required
def delete(request, id):
    memory = get_object_or_404(Memory, id=id, owner=request.user)
    
    if request.method == 'POST':
        memory.delete()
        return redirect('memories')
    
    return render(request, 'memories/confirm_delete.html', {'memory': memory})