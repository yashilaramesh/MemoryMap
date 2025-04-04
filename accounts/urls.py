from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup, name='accounts.signup'),
    path('login/', views.login, name='accounts.login'),
    path('logout/', views.logout, name='accounts.logout'),
    path('resetpassword', views.resetpassword, name='accounts.resetpassword'),
    path('account/', views.account, name='account'),  # Keep only this one for account management
]
