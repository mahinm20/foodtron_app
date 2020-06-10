from django.shortcuts import render
from restaurant.models import ChineseMenu, IndianMenu, PizzaMenu, IceCreamMenu
# Create your views here.

def chinese_menu(request):
    chinese = ChineseMenu.objects.all()
    return render(request,'restaurant/chinese_menu.html',{'chinese':chinese})

def indian_menu(request):
    indian = IndianMenu.objects.all()
    return render(request,'restaurant/indian_menu.html',{'indian':indian})

def pizza_menu(request):
    pizza = PizzaMenu.objects.all()
    return render(request,'restaurant/pizza_menu.html',{'pizza':pizza})

def ice_cream_menu(request):
    ice_cream = IceCreamMenu.objects.all()
    return render(request,'restaurant/ice_cream_menu.html',{'ice_cream':ice_cream})
