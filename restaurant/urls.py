from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('chinese',views.chinese_menu,name='chinese'),
    path('indian',views.indian_menu,name="indian"),
    path('ice_cream',views.ice_cream_menu,name='ice_cream'),
    path('pizza',views.pizza_menu,name="pizza"),
    
]