from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
from django.contrib import messages
# Create your views here.

def index(request):
    return render (request, "index.html")

def home(request):
    
    context = {
        "userb" : Userinfo.objects.get(user=request.user)
    }
    return render (request, "home.html",context)

def userProfile(request):
    return render (request, "userprofile.html")

def discover(request):
    return render (request, "discover.html")

def register(request):
    
    if request.method == "POST" :
        
        name = request.POST["name"]        
        username = request.POST["username"]
        
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        bdate = request.POST["bdate"]
        agree = request.POST["agree"]
        
        if password1 == password2:
            if User.objects.filter(username=username).exists(): # exists varsa true döndürür
                alertUsername = "is-invalid"
                return render(request, 'index.html', {"alertUsername": alertUsername})            
                        
            else:                
                # KAYDOL start
                user = User.objects.create_user( first_name=name, username=username , password=password1)
                user.save()
                userinfo = Userinfo(user=user, agree=agree, bdate=bdate,)
                userinfo.save()
                
                # KAYDOL end
                messages.success(request, 'Kaydınız tamamlanmıştır.')
                return redirect('login')
    
    return render (request, "register.html")

def loginUser(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(username=username ,password=password)
                
        if user is not None:
            login(request,user)    
                    
            return redirect('home')
        else:
            messages.error(request, 'Hatalı Kullanıcı Adı veya Şifre')
            return redirect('login')
    
    return render (request, "login.html")

# ------------ ÇIKIŞ ----------------------------------------------
def userLogout(request):  
    logout(request)
    return redirect('/')
# ------------ ÇIKIŞ ----------------------------------------------
