from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("infor", views.news),
    path("khoahoc", views.khoahoc),
    path("contact/", views.contact),
]
