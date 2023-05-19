from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.loginuser,name='login'),
    path('reg/',views.register,name='register')
]