from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
urlpatterns = [
    path('', views.say_hello, name='index'),
    path('main/', views.main, name='main'),
    path('encryption/', views.encryption, name='encryption'),
    path('decryption/', views.decryption, name='decryption'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
]      
