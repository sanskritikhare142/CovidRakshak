from django.shortcuts import render
import requests
import json
from django.contrib.auth.forms import UserCreationForm

def login(request):
    form= UserCreationForm()
    context = {'form': form}
    return render(request, 'app1/login.html', context)

def signin(request):
    form= UserCreationForm()

    if request.method == 'POST':
        form= UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'app1/signin.html', context)

def home(request):
    r = requests.get("http://gsx2json.com/api?id=1aLH0dQFW3mN5vSxJdhjdQuAMTKojCDn-7mk6CNH3W68&sheet=1")
    j=r.json()
    
    
    return render(request, 'app1/home.html', j)


def database(request):
    re= requests.get("http://gsx2json.com/api?id=104iTkc01Gnq79wi0ax1PmbDWZgwFqYGgiJovzF7zLMI&sheet=1")
    je= re.json()
    
    return render(request, 'app1/database.html', je)

def violations(request):
    req= requests.get("http://gsx2json.com/api?id=1P9rD3Ce0iHJqQHko6MrwNCGLTlx3jFt8DTldhsKOs_0&sheet=1")
    jeq= req.json()
    
    return render(request, 'app1/violations.html', jeq)



    
