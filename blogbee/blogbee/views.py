from turtle import home
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

def Home(request):

    # return HttpResponse('Home_view')
    return render(request,'home.html')

def login_view(request):
    if request.method == "POST":
        form=AuthenticationForm(request.POST)
        if form.is_valid():
            user=form.get_user
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                 return redirect('articles:list')

    else:
        form = AuthenticationForm()
    # return HttpResponse('login_view')
    return render(request,'login.html',{'form':form})


def signup_view(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            #log user in
            return redirect('articles:list')
    else:    
        form = UserCreationForm(request)
    # return HttpResponse('signup_view')
    return render(request,'signup.html',{'form':form})

def article(request):
    # return HttpResponse('article_view')
    return render(request,'article.html')

