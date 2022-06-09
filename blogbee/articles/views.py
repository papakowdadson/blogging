from django.shortcuts import render
from .models import Articles

def articles_list(request):
    Article= Articles.objects.all().order_by('Date')
    return render(request,'articles/articles_list.html',{'Article':Article})
