from django.db import models

from commen.models import Restaurant

# Create your models here.

class Category(models.Model):
    catg_name =models.CharField(200)
    discription =models.CharField(400)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)

class Menu(models.Model):
    item_name = models.CharField(200)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    food_type = models.CharField(200)
    price = models.FloatField()
    image = models.ImageField(upload_to='restaurant/')
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)

