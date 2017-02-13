# coding=utf-8

from django.shortcuts import render
from tourist.models import Tourist

# Create your views here.

def index(request):
    context = {
        'Tourist': Tourist
    }
    return render(request, 'tourist/base.html', context)

def tourist(request):
    return render(request, 'tourist/detail/tourist_detail.html')