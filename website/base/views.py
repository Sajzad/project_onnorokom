from django.shortcuts import render, HttpResponse

from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required

from .models import *

def home_view(request):
    
    context = {}

    return render(request, 'base/index.html', context)

@login_required
def dashboard_view(request):
    
    context = {}

    return render(request, 'base/dashboard.html', context)

@login_required
def video_watch_view(request, video_id):
    
    context = {}

    return render(request, 'base/video-watch.html', context)

@login_required
def myvideos_view(request, username):
    
    context = {}

    return render(request, 'base/myvideos.html', context)

