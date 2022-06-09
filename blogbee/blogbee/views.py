from django.http import HttpResponse
from django.shortcuts import render

def Home(request):

    # return HttpResponse('Home_view')
    return render(request,'home.html')

def login(request):
    # return HttpResponse('login_view')
    return render(request,'login.html')


def signup(request):
    # return HttpResponse('signup_view')
    return render(request,'signup.html')

def article(request):
    # return HttpResponse('article_view')
    return render(request,'article.html')