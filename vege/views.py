from django.shortcuts import render , redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required



@login_required(login_url="/login_page")
def recepies(request):

    if request.method == "POST":

     data=request.POST
     recepie_imp= request.FILES.get("recepie_imp")
     recepie_name= data.get("recepie_name")
     recepie_desc= data.get("recepie_desc")


     recepie.objects.create(
        recepie_name=recepie_name,
        recepie_desc=recepie_desc,
        recepie_imp=recepie_imp,
     )
     return redirect("recepie")
    
    
     
   
    return render(request,"recepie.html")


@login_required(login_url="/login_page")
def viewrec(request):
    queryset= recepie.objects.all()
    
    
    
    if request.GET.get('search'):
       queryset=queryset.filter(recepie_name__icontains = request.GET.get('search'))
       context={'recepie':queryset}

    else:
        queryset1 = recepie.objects.all()
        context={'recepie':queryset1}

       


    
    return render(request,"viewrec.html",context)

@login_required(login_url="/login_page")
def delete(request, id):
   queryset= recepie.objects.get(id=id)
   queryset.delete()
   return redirect("viewrec")


@login_required(login_url="/login_page")
def update(request,id):
   queryset=recepie.objects.get(id=id)
   context={'recepie': queryset}
   
   if request.method == "POST":
        data=request.POST
        recepie_imp= request.FILES.get("recepie_imp")
        recepie_name= data.get("recepie_name")
        recepie_desc= data.get("recepie_desc")

        queryset.recepie_name=recepie_name
        queryset.recepie_desc=recepie_desc
        

        if recepie_imp:
          queryset.recepie_imp=recepie_imp

        queryset.save()
        return redirect("viewrec")

   return render(request,"update.html",context)


def login_page (request):
  
  if request.method == "POST":
     username=request.POST.get('username')
     password= request.POST.get('password')

     if not User.objects.filter(username=username).exists():
       messages.error(request,"INVALID USERNAME")
       return redirect("login_page")
 
   
     user1 =authenticate(username=username,password=password)
     if user1 is None:
        messages.error(request,"Invalid password")
        return redirect("login_page")
     
     else :
        login(request,user1)
        return redirect("recepie")
        

  return render(request,"login_page.html")


def register (request):
  
  if request.method == "POST":
     fname=request.POST.get("fname")
     lname=request.POST.get("lname")
     username=request.POST.get("username")
     password=request.POST.get("password")
     
     user1 = User.objects.filter(username=username)
    
     
     if user1.exists():
        messages.info(request,"username not avilable")
        return redirect("register")
     

     user= User.objects.create(
      first_name=fname,
      last_name=lname,
      username=username 
      )
     user.set_password(password)
     user.save()
     messages.info(request,"account created successfully")
     return redirect("register")
   

  return render(request,"register.html")

def logout_page(request):
 logout(request)
 return redirect("login_page")

def home(request):
   return render(request,"home.html")