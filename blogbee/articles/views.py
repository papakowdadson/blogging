from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Articles
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from . import forms

def articles_list(request):
    Article= Articles.objects.all().order_by('Date')
    return render(request,'articles/articles_list.html',{'Article':Article})

def articles_detail(request,slug):
    return HttpResponse(slug)

def logout_view(request):
    if request.method == "POST":
        logout('request')
        return redirect('login')

@login_required(login_url='login/')
def create(request):
    if request.method == "POST":
        form = forms.CreateArticles(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.Author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticles()
    return render(request,'articles/create.html',{'form':form })