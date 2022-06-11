from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Articles
from django.contrib.auth import logout

def articles_list(request):
    Article= Articles.objects.all().order_by('Date')
    return render(request,'articles/articles_list.html',{'Article':Article})

def articles_detail(request,slug):
    return HttpResponse(slug)

def logout_view(request):
    if request.method == "POST":
        logout('request')
        return redirect('login')