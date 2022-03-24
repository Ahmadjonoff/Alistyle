from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('bolim/', BolimView.as_view(), name='category'),
    path('bolim/<str:nom>/', IchkiView.as_view(), name='ichki'),
    path('ichki/<str:nom>/', MahsulotView.as_view(), name='mahsulotlar'),
    path('home/', Home2.as_view(), name='home'),
    path('product/<str:nom>/', Product.as_view(), name='product'),
    path('index/', Index.as_view(), name='index'),
]