from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import include,url

urlpatterns = [
   path('addtocart/',views.cartView.as_view() ),
   #path('products/<int:pid>',views.single_productView.as_view() ),
   

  
]