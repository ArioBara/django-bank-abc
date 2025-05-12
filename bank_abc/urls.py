from django.contrib import admin
from django.urls import path
from . import views

app_name = 'bank_abc'

urlpatterns = [
    path('', views.tampildata),
    path('inputdata/',views.inputdata),
    path('simpandata',views.simpandata),
    path('hapusdata/<int:id>',views.hapusdata),
    path('editdata/<int:id>',views.editdata),
    path('updatedata/<int:id>',views.updatedata)    
]