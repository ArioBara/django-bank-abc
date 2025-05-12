from unicodedata import name
from django.urls import URLPattern, path
from . import views

app_name = 'bank_abc'

urlpatterns = [
    path('', views.index),
    path('dash/', views.dash),
    path('pembelian/', views.pembelian),
    path('transfer/', views.transfer),
    path('transaksi/', views.transaksi),
    path('akun/', views.akun),
    path('struk/', views.struk),
    path('login/', views.login),
    path('simpandata',views.simpandata),
    path('editakun/<int:id>',views.editakun),
    path('updateakun/<int:id>',views.updateakun)
]