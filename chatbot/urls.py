from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatbot_page, name='chatbot'),
    path('query/', views.chatbot_query, name='chatbot_query'),
]

