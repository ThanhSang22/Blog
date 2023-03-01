from django.urls import path 
from . import views 

urlpatterns = [ 
    path('', views.index),
    path('news', views.index1) ,
    path('khoahoc', views.index2),
    path('contact/', views.contact),
]
