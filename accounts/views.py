from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

import csv
from django.http import HttpResponse

# Create your views here.
def Signpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username,email=email,password=password)
        user.save()
        messages.success(request,'Your Acount has been created successfully')
        return redirect('Login')
    return render(request,'accounts/signup.html')

def Loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate (username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'You are successfully login ')
            return redirect('Blogpage')
        else:
            messages.warning(request,'Invalid creadential found ')
    return render(request,'accounts/login.html')

def logout_user(request):
    messages.success(request,'Your Successfully Logout ')
    logout(request)
    return redirect('Login')


def download_csv(request):
    response = HttpResponse(content_type="text/csv")
    headers={"Content-Disposition": 'attachment; filename="users.csv"'}

    writer = csv.writer(response)
    writer.writerow(["Username", "Email"])

    users = User.objects.all().values_list('username','email')

    for user in users:
        writer.writerow(user)

    return response