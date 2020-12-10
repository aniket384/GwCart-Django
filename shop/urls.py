from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackinStatus"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productView, name="ProductViews"),
    path("checkout/", views.checkout, name="checkout"),
]