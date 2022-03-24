from django.urls import path, include
from .views import *

urlpatterns = [
    path('payment/', Payment.as_view(), name = 'payment'),
    path('profile_orders/s', Profile_orders.as_view(), name = 'orders'),
    path('wishlist/', Wishlist.as_view(), name = 'tanlangan'),
    path('shopping_cart/', Shopping_cart.as_view(), name = 'savat'),
    path('savat/<str:nom>/', SavatQoshView.as_view(), name = 'savat_qosh'),
    path('savatdan_ochir/<int:id>/', SavatOchirView.as_view(), name = 'savat_ochir'),
    path('wishdan_ochir/<int:id>/', WishOchirView.as_view(), name = 'wish_ochir'),
    path('wishlist/<str:nom>/', AddToWishList.as_view(), name = 'wishlist_qosh'),
]
