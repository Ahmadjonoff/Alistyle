from django.shortcuts import render
from django.views import View

from .models import *


class Home(View):
    def get(self, request):
        return render(request, 'page-index-2.html')

class Home2(View):
    def get(self, request):
        bolimlar = Bolim.objects.all()
        return render(request, 'page-index.html', {'bolimlar' : bolimlar})

class BolimView(View):
    def get(self, request):
        bolimlar = Bolim.objects.all()
        return render(request, 'page-category.html', {'bolimlar' : bolimlar})
class IchkiView(View):
    def get(self, request, nom):
        bolim = Bolim.objects.get(nom=nom)
        ichki = Ichki.objects.filter(bolim=bolim)
        return render(request, 'ichki.html', {'ichkilar' : ichki})

class Product(View):
    def get(self, request, nom):
        mahsulot = Mahsulot.objects.get(nom = nom)
        return render(request, 'page-detail-product.html', {'mahsulot' : mahsulot})

class Index(View):
    def get(self, request):
        return render(request, 'page-index-2.html')

class MahsulotView(View):
    def get(self, request, nom):
        ichki = Ichki.objects.get(nom = nom)
        return render(request, 'page-listing-grid.html', {'ichki' : ichki})