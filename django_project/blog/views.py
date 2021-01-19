from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    post = Post.objects.all()
    return render(request,'blog/home.html',{'posts':post})

@login_required
def about(request):
    return render(request,'blog/about.html',{'title':'django_about'})
