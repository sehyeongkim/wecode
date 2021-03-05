from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=20)

class Category(models.Model):
    name = models.CharField(max_length=20)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

class Drink(models.Model):
    category  = models.ForeignKey('Category', on_delete = models.CASCADE)
    name      = models.CharField(max_length=50)

class Image(models.Model):
    image_url = models.CharField(max_length=2000)
    drink     = models.ForeignKey('Drink', on_delete = models.CASCADE)

class Allergy(models.Model):
    name = models.CharField(max_length = 20)

class AllergyDrink(models.Model):
    allergy = models.ForeignKey('Allergy',on_delete = models.CASCADE)
    drink   = models.ForeignKey('Drink', on_delete = models.CASCADE)

