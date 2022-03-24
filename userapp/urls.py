from django.urls import path
from .views import *

from asosiy.views import *

urlpatterns = [
    path('address/', Address.as_view(), name = 'address'),
    path('main/', Main.as_view(), name = 'main'),
    path('setting/', Setting.as_view(), name = 'setting'),
    path('login/', Login.as_view(), name = 'login'),
    path('register/', Register.as_view(), name = 'register'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
]
