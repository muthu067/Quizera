import logging
from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse
from django.urls import reverse
from .models import course, about_us
from django.core.paginator import Paginator
from .forms import ContactForm,Register_Form,Login
from django.contrib import messages
from django.contrib.auth import authenticate ,login as auth_login , logout as auth_logout
from django.contrib.auth.decorators import login_required

def login(request):
    if request.user.is_authenticated:
        logout(request)
    if request.method =='POST':
        form=Login(request.POST)
        username=request.POST.get('username')
        if form.is_valid():
            print('success')
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user is not None :
                auth_login(request,user)
                print("auth success")
                return redirect("/home")
        else:
            print("failed")
            return render(request,'login.html',{'form':form ,'username':username})
    return render(request,'login.html')

@login_required(login_url='blog:login')
def home(request):

    # course=[
    #     {'cname':'python course','cid':1},
    #     {'cname':'java course','cid':2}
    # ]
    # Logger=logging.getLogger("Testing")
    # Logger.debug(f'checking variable is{course}')


    all_pages=course.objects.all()
    paginator=Paginator(all_pages,5)
    page_num=request.GET.get('page')
    page_obj=paginator.get_page(page_num) 

    return render(request,'index.html',{'page_obj':page_obj})

@login_required(login_url='blog:login')
def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)

        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')

        logger=logging.getLogger('Testing')
        if form.is_valid():
            logger.debug(f'ex: {form.cleaned_data['name']}')
            succes='Your email is sent successfully'
            return render(request,'contact.html',{'form':form,'success':succes})
        else:
            logger.debug('Form validation failed')
            return render(request,'contact.html',{'form':form,'name':name,'email':email,'message':message})
    return render(request,'contact.html')

@login_required(login_url='blog:login')
def detail(request,slug):
    try:
        id_n=course.objects.get(slug=slug)
    except course.DoesNotExist:
        raise Http404("course doesn't exist")
    return render(request,'detail.html',{'courses':id_n})
    # return HttpResponse(f'<h1> viewing course id {id_no} and course name {id_n} <h1>')

def old_url(request):
    return redirect(reverse("blog:new_url"))

def new_url(request):
    return HttpResponse("<h1>have you redirected from old ?</h1>")

@login_required(login_url='blog:login')
def about(request):
    content=about_us.objects.first()
    if content is None or not content.content:
        content='No about us'
    else:
        content=content.content
    return render(request,'about.html',{'content':content})

@login_required(login_url='blog:login')
def register(request):
    if request.method=='POST':
        form=Register_Form(request.POST)
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request,'Registration Success. You can login now!')
        
        else:
            return render(request,'register.html',{'form':form,'username':username,'email':email})
    return render(request,'register.html')

def logout(request):
    auth_logout(request)
    return redirect('blog:login')