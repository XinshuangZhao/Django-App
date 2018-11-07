from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('index/', views.showinfo, name='showinfo'),
    path('transfer/', views.transfer, name='transfer'),
    path('redeem/', views.redeem, name='redeem'),
]
