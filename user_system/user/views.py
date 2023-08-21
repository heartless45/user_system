from django.shortcuts import render,redirect
from django.contrib.auth import logout
from .models import User
from .forms import RegistnationForm



# Create your views here.
def home_view(request):
    return render(request,'home.html')

def Registnation_view(request):
    if request.method == "POST":
        form = RegistnationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if data['password'] == data['confirm_password']:
                user = User(
                    first_name=data['first_name'],
                    last_name=data['last_name'],
                    email=data['email'],
                    password=data['password']
                )
                user.save()
                return redirect('home')
    else:
        form = RegistnationForm()
    return render(request,'registration.html',{'form':form})