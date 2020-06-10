from django.db import models

# Create your models here.
class ChineseMenu(models.Model):
    name_of_dish = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name_of_dish

class IndianMenu(models.Model):
    name_of_dish = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name_of_dish

class PizzaMenu(models.Model):
    name_of_dish = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name_of_dish

class IceCreamMenu(models.Model):
    name_of_dish = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name_of_dish                