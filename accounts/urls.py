<<<<<<< HEAD
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('accounts.urls')),
    path('admin/', admin.site.urls),
]
=======
from django.urls import path
from . import views

urlpatterns = [
    path('accounts/', views.accounts, name='accounts'),
]
>>>>>>> 4f22921 (maps and accounts)
