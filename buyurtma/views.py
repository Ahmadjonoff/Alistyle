from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.views import View
from userapp.models import *
from .models import *
from asosiy.models import *


class Payment(View):
    def get(self, request):
        return render(request, 'page-payment.html')

class Profile_orders(View):
    def get(self, request):
        return render(request, 'page-profile-orders.html')

class Wishlist(View):
    def get(self, request):
        mijoz = Mijoz.objects.get(user=request.user)
        wish = Tanlangan.objects.filter(mijoz = mijoz)
        return render(request, 'page-profile-wishlist.html', {'wish' : wish})

class Shopping_cart(View):
    def get(self, request):
        if request.user.is_authenticated:
            mijoz = Mijoz.objects.get(user = request.user)
            shopping = Savat.objects.filter(mijoz = mijoz)
            return render(request, 'page-shopping-cart.html', {'shopping' : shopping})
        else:
            return redirect('login')

class SavatQoshView(View):
    def get(self, request, nom):
        if request.user.is_authenticated:
            mijoz = Mijoz.objects.get(user = request.user)
            m = Mahsulot.objects.get(nom = nom)
            Savat.objects.create(
                mijoz = mijoz,
                mahsulot = m
            )
            return redirect('product', m.nom)
        else:
            return redirect('login')

class SavatOchirView(View):
    def get(self, request, id):
        Savat.objects.get(id = id).delete()
        return redirect('savat')

class AddToWishList(View):
    def get(self, request, nom):
        mijoz = Mijoz.objects.get(user=request.user)
        m = Mahsulot.objects.get(nom=nom)
        Tanlangan.objects.create(
            mijoz = mijoz,
            mahsulot = m
        )
        return redirect('savat')

class WishOchirView(View):
    def get(self, request, id):
        Tanlangan.objects.get(id = id).delete()
        return redirect('tanlangan')