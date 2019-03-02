from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import include,url

urlpatterns = [
   path('category/',views.categoryView.as_view() ),
   path('products/',views.productView.as_view() ),
   path('products/<int:pid>',views.single_productView.as_view() ),
   path('category/products/<int:cid>',views.catwise_productView.as_view() ),

  
]