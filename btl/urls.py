from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="test"),
    path("shop-cart", views.shopcart, name="shop-cart"),
    path("checkout", views.checkout, name="checkout"),
    path("login", views.login, name="login"),
    path("logout", views.logout,name="logout")
]
