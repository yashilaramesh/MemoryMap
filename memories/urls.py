from django.urls import path
from . import views
urlpatterns = [
    path('memories/', views.memoriesMethod, name='memories'),
    path('<int:id>/', views.show, name = 'memories.show'),
]