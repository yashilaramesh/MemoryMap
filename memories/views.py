from django.shortcuts import render

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

def memoriesMethod(request):
    template_data = {}
    template_data['title'] = 'Memories'
    template_data['memories'] = memories
    return render(request, 'memories/index.html',
                  {'template_data': template_data})

#this is a comment for github purposes