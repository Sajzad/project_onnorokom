from django.shortcuts import render, HttpResponse

from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required

from .models import *

@login_required
def home_view(request):
    
    context = {}

    return render(request, 'base/index.html', context)

