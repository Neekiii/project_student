from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from  django.core.mail import send_mail
from django.conf import settings
# Create your views here.
class LoginView(View):
    def get(self,request):
        return render(request,'accounts/login.html')
    
    def post(self,request):
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'login success')
            return redirect('dashboard')
        messages.error(request,'login fail')
        return redirect('login')
    
class LogoutView(View):
    def get(self,request):
        logout(request)
        messages.success(request,'logout success')
        return redirect('login')

class RegisterView(View):
    def get(self,request):
        return render(request,'accounts/register.html')
    
    def post(self,request):
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')

        try:
            user = User.objects.create_user(email=email,username=username,password=password)
       
            if user is not None:
                user.first_name = first_name
                user.last_name = last_name
                user.is_active = True
                user.save()
                
                send_mail(
                    'Account Creation',
                    'Your account has been created successfully,welcome tpo SES',#body
                    settings.EMAIL_HOST_USER,#sender mail address
                    [user.email]#receive email address
                )
                messages.success(request,'register success')
                return redirect('login')
            messages.error(request,'something went wrong')
            return redirect('register')
        except:
            messages.error(request,'something went wrong')
            return redirect('register')

class DashboardView(View):
    
    def get(self,request):
        if not request.user.is_authenticated:
            messages.error(request,'unauthorized access')
            return redirect('login')
        return render(request,'dashboard.html')