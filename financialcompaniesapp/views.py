# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .forms import UserRegistrationForm,LoginForm,ViewDatadbForm
from .models import UserRegistration,CompanySales
from django.shortcuts import redirect
from django.contrib import messages


def home(request):
    return render(request, 'home.html',)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form =UserRegistrationForm()
            return render(request,'registration.html',{'form':form})
    else:
        form=UserRegistrationForm()
        return render(request, 'registration.html',{'form':form})


def login(request):
    form = LoginForm(request.POST)
    if request.method == "POST":
        username = request.POST.get('username')
        pword = request.POST.get('password')
        dbuser = UserRegistration.objects.filter(username=username,password=pword)
        if not dbuser:
            return render(request, 'login.html',{'form':form})
        else:
            return redirect('ViewDatadb')
    else:
       form = LoginForm()
       return render(request, 'login.html',{'form':form})


def ViewDatadb(request):
    form=ViewDatadbForm()
    if request.method == "POST":
        form=ViewDatadbForm(request.POST)
        companyname=request.POST.get('companyname')
        obj=CompanySales.objects.get(Companyname=companyname, )      
        if not obj:
            return render(request, 'viewdata1.html',{'form':form})
        else:
            obj=CompanySales.objects.get(Companyname=companyname)      
            return render(request, 'viewdatapage1.html',{'obj':obj})
    else:
        form=ViewDatadbForm()
        return render(request, 'viewdata1.html',{'form':form})


        
def ViewDatadb1(request):
    form=ViewDatadbForm()
    if request.method == "POST":
        form=ViewDatadbForm(request.POST)
        companyname=request.POST.get('companyname')
        obj=CompanySales.objects.get(Companyname=companyname)      
        if not obj:
            return render(request, 'viewdata1.html',{'form':form})
        else:
            obj=CompanySales.objects.get(Companyname=companyname)      
            return render(request, 'viewdatapage1.html',{'obj':obj})
    else:
        form=ViewDatadbForm()
        return render(request, 'viewdata1.html',{'form':form})

