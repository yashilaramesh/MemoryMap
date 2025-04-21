from django.urls import path
from . import views
urlpatterns = [
    path('memories/', views.index, name='memories'),
    path('locations/', views.memory_locations, name='memory_locations'),
    path('<int:id>/', views.show, name = 'memories.show'),
    path('<int:id>/edit/', 
         views.edit, name='memories.edit'),
    path('<int:id>/delete/', views.delete, name='memories.delete'),
    path('memories/create/', views.create_memory, name='memories.create'),
]