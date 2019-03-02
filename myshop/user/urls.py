from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import include,url

urlpatterns = [
    path('register/<int:id>',views.resisterView.as_view() ),
    path('register',views.resisterView.as_view() ),
   path('login/',views.userView.as_view() ),
   #path('login/',views.loginView.as_view() )

  
]
