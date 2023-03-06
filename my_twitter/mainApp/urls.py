from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('discover/', views.discover, name='discover'),
    path('userprofile/', views.userProfile, name='userprofile'),
    
    
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    
    
]