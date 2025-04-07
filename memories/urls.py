from django.urls import path
from . import views
urlpatterns = [
    path('memories/', views.index, name='memories'),
    path('<int:id>/', views.show, name = 'memories.show'),
]