from django.urls import path
from . import views
urlpatterns = [
    path('memories/', views.memoriesMethod, name='memories'),
]