from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
# Create your views here.
from django.contrib.auth.decorators import login_required


def Aboutpage(request):
    return render(request,'pages/about.html')


def Contactpage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email  = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        con = Contactm(name=name,email=email,subject=subject,message=message)
        con.save()
        return redirect('Contact')

    return render(request,'pages/contact.html')

