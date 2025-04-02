from django.urls import path
from . import views


urlpatterns = [
    path('signup', views.signup, name = 'accounts.signup'),
    path('login/', views.login, name = 'accounts.login'),
    path('logout/', views.logout, name = 'accounts.logout'),
    path('resetpassword', views.resetpassword, name='accounts.resetpassword'),
    path('change-username/', views.change_username, name='accounts.change_username'),
    path('change-password/', views.change_password, name='accounts.change_password'),

   ]
