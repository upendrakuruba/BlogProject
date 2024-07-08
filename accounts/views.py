from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
import csv
from django.http import HttpResponse

# Create your views here.
def Sign_page(request):
 if request.method == 'POST':
  username = request.POST.get('username')
  email = request.POST.get('email')
  password1 = request.POST.get('password1')
  password2 = request.POST.get('password2')
  if password1 == password2:
   if User.objects.filter(username=username).exists():
    messages.info(request,"Username Token")
    return render(request, 'accounts/signup.html')
   elif User.objects.filter(email=email).exists():
    messages.info(request,"Email Token")
    return render(request, 'accounts/signup.html')
   else:
      user = User.objects.create_user(username=email,first_name=username,email=email,password=password1)
      user.save()
      messages.success(request,"Your account has been Register Successfully!")
      return redirect("Login")
  else:
   messages.info(request,"Password Not Matched")
   return render(request, 'accounts/signup.html')
 else:
   return render(request, 'accounts/signup.html')

def Login_page(request):
 if request.method == 'POST':
  username = request.POST.get('email')
  password = request.POST.get('password')
  user = authenticate(username=username,password=password)
  if user is not None:
   login(request,user)
   if 'next' in request.POST:
    messages.info(request,'Successfully Login')
    return redirect(request.POST.get('next'))
   else:
    return redirect('Blogpage')
  else:
   messages.info(request,'User name or Password not Match')
   return render(request, 'accounts/login.html')
 else:
   return render(request, 'accounts/login.html')

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