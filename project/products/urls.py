from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.choosetype,name='choosetype'),
    path('industrial/',views.industrial,name='industrial'),
    path('commercial/',views.commercial,name='commercial')

]