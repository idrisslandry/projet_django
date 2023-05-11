from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('machines/',views.machine_list_view,name='machines'),
    path('personnels/',views.personnel_list_view , name='personnels'),
    path('machine/<pk>',views.machine_detail_view,name='machine-detail'),
    
    
]