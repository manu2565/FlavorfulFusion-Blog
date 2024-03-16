from tkinter import SE
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login
from django.contrib import messages


from contactenquriry.models import Post, contactEnquiry,singlepost,SubPlan,SubPlanFeature,Posts

from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import logout
from contactenquriry.models import Post,Services
from django.views.generic import ListView,DetailView
from django.contrib.auth.decorators import login_required

from django.utils import timezone



from datetime import datetime, timedelta

def index(request):
    #icontains-oneletter search
    servicesData=Services.objects.all()

 
    if request.method=="GET":
        st=request.GET.get('servicename')
        if st!=None:
             servicesData=Services.objects.filter(service_title__icontains=st)

    data={'servicesData':servicesData}
    
    return render(request,"index.html",data)

def header(request):
   
    return render(request,"header.html")

def footer(request):
    return render(request,"footer.html")

def base(request):
    return render(request,"base.html")

def category(request):
    return render(request,"category.html")


def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        messages=request.POST.get('message')

        em=contactEnquiry(name=name,email=email,subject=subject,messages=messages)
        em.save()
        return redirect('home')
    return render(request,"contact.html")     

def saveEnquiry(request):
    pass
   
def searchresult(request):
    return render(request,"search-result.html")






@ensure_csrf_cookie
def single_post(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

    
        nm = singlepost.objects.create(name=name, email=email, message = message)
        nm.save() 

    return render(request, "single-post.html")




def aboutpage(request):
    return render(request,"about.html")



def login(request):
    if request.method == "POST":
        username=request.POST.get('username')
        pass1=request.POST.get('Password1')


        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            auth_login(request,user)
            fname=user.first_name
            return render(request,"index.html",{'fname':fname})

        else:
            messages.error(request,"Bad Creadentials!")

        return redirect('home')

    return render(request,"login.html")

def singin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname=request.POST.get("lname")
        email = request.POST.get('email')
        pass1 = request.POST.get('Password1')
        pass2 = request.POST.get('Password2')

        if User.objects.filter(username=username):
            messages.error(request,"Username already exist! Please try some other username")
            return redirect('home')
        if User.objects.filter(email=email):
            messages.error(request,"email already exist! Please try some other email")
            return redirect('login')

        if len(username)>10:
            messages.error(request,"Username must be under 10 charecters")

        if pass1 != pass2:
            messages.error(request,"Password didn't match")
        
        if not username.isalnum():
            messages.error(request,"username must be Alpha-Numberic!")
            return redirect('home')

        my_user=User.objects.create_user(username,email,pass1)
        my_user.first_name=fname
        my_user.last_name=lname
        my_user.save()  
    
        return redirect('login')
    
         
        
    return render(request,"singin.html")



def home(request):
    return render(request,"home.html")


class HomeView(ListView):
    model = Post
    template_name="post.html"


def signout(request):
    logout(request)
    return redirect('home')










#Subscription Plane
def pricing(request):
   
    pricing_plans = SubPlan.objects.all()
    

    distinct_features = SubPlanFeature.objects.values('title').distinct()
   
    return render(request, 'pricing.html', {'plans': pricing_plans, 'dfeatures': distinct_features})







def read(request, post_id):
    if post_id:
        post = Posts.objects.filter(pk=post_id)

    return render(request=request, template_name='read.html', context={'post': post.get()})


def update(request, post_id):
    if post_id:
        post = Posts.objects.filter(pk=post_id)
    if request.POST:
        n_t = request.POST['title']
        n_c = request.POST['content']
        post.update(title=n_t, content=n_c)
        return redirect('/')
    return render(request=request, template_name='update.html', context={'post': post.get()})


def delete(request, post_id):
    if post_id:
        p = Posts.objects.filter(pk=post_id)
        p.delete()
        return HttpResponse('Post has been successfully deleted')
    return HttpResponse('insert a post id to delete')


def create(request):
    if request.POST:
        title = request.POST['title']
        content = request.POST['content']
        Posts.objects.create(title=title, content=content)
        return redirect('/')
    return render(request=request, template_name='create.html', context={})





def indexes(request):
    data = Posts.objects.all()
    return render(request=request, template_name='indexes.html', context={'data': data})