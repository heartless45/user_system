from django.shortcuts import render,redirect
from django.contrib.auth import logout
from .models import User



# Create your views here.
def home_view(request):
    return render(request,'home.html')