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
        "twitts": Twitts.objects.order_by("-id"),
        "userb" : Userinfo.objects.get(user=request.user)
    }
    
    if request.method == "POST" and 'btntwitt' in request.POST:
        user = request.user
        userinfo = Userinfo.objects.get(user=request.user)
        twitt_header = "baslık yok"
        twitt = request.POST["twitt"]
        like = 0
        retweet = 0
        try:
            media = request.FILES["twittmedia"]       
        except:
            media = None       
    
        twitted = Twitts(user = user, 
        userinfo = userinfo, 
        twitt_header = twitt_header ,
        twitt = twitt,
        like = like,
        retweet = retweet,
        media = media)
        twitted.save()  
        print(twitt)
        
        
    if request.method == "POST" and 'btnlike' in request.POST:
       
        twittid = request.POST["liked"]
        selectedtwitt = Twitts.objects.get(id=twittid)
        liked = selectedtwitt.like
        liked +=1 
        tliked = Twitts.objects.filter(id=twittid).update(like=liked)
        
        
        print("sssssa",tliked)
        
        
            
        
        
    return render (request, "home.html",context)

def userProfile(request):
    context = {
        "userb" : Userinfo.objects.get(user=request.user)
    }
    return render (request, "userprofile.html",context)

def discover(request):
    
    try:
        context = {
            "userb" : Userinfo.objects.get(user=request.user)
        }
    except:
        context = {
            
        }
    return render (request, "discover.html",context)

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
