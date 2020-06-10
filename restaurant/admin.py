from django.contrib import admin

# Register your models here.
from restaurant.models import IceCreamMenu, PizzaMenu, ChineseMenu, IndianMenu

admin.site.register(IceCreamMenu)
admin.site.register(PizzaMenu)
admin.site.register(ChineseMenu)
admin.site.register(IndianMenu)