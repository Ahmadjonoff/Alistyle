from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from .models import *
from django.core.mail import send_mail
from django.conf import settings

class Address(View):
    def get(self, request):
        return render(request, 'page-profile-address.html')

class Main(View):
    def get(self, request):
        if request.user.is_authenticated:
            user = Mijoz.objects.get(email=request.user.username)
            return render(request, 'page-profile-main.html', {'user' : user})
        else: return redirect('login')

class Setting(View):
    def get(self, request):
        return render(request, 'page-profile-setting.html')

class Login(View):
    def get(self, request):
        return render(request, 'page-user-login.html')
    def post(self, request):
        user = authenticate(
            username = request.POST['login'],
            password = request.POST['parol']
        )
        if user is None:
            return redirect('login')
        else:
            login(request, user)
            return redirect('home')

class Register(View):
    def get(self, request):
        return render(request, 'page-user-register.html')
    def post(self, request):
        if request.POST['parol'] == request.POST['parol']:
            u = User.objects.create_user(
                username = request.POST['email'],
                password = request.POST['parol']
            )
            Mijoz.objects.create(
                ism = request.POST['f'] + ' ' + request.POST['l'],
                email = request.POST['email'],
                jins = request.POST['jins'],
                tel = request.POST.get('tel'),
                user = u,
                shahar = request.POST['sh'],
                mamlakat = request.POST['m'],
            )
            subject = 'Alistyle'
            message = ' Alistylega xush kelibsiz! '\
                        'Maroqli xarid tilaymiz!'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST['email'], ]
            send_mail(subject, message, email_from, recipient_list)

            return redirect('/user/login/')
        else:
            return redirect('register')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')