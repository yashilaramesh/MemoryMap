from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('resetpassword', views.resetpassword, name='resetpassword'),
    path('account/', views.account, name='accounts'),  # Keep only this one for account management
]