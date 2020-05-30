from django.shortcuts import render, HttpResponse
import ee
ee.Initialize()
import os
# Create your views here.

def index(request):
    
    return render(request,'index.html')

def index_calculation(a,b):
    return a.subtract(b).divide(a.add(b))
