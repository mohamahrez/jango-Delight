from django.db import models

# Create your models here.
class Ingredient(models.Model):
  name = models.CharField(max_length=30,null=True,blank=True,unique=True)
  quantity = models.FloatField(null=True, blank=True, default=0.0)
  unit = models.CharField(max_length=30,null=True,blank=True)
  unit_price = models.FloatField(null=True, blank=True, default=0.0)
'''   def get_absolute_url(self):
        return "/ingredients"'''




class MenuItem(models.Model):
  title=  models.CharField(max_length=30,null=True,blank=True,unique=True)
  price = models.FloatField(null=True, blank=True, default=0.0)
'''     def get_absolute_url(self):
        return "/menu"'''


class RecipeRequirement(models.Model):
  menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
  ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
  quantity = models.FloatField(null=True, blank=True, default=0.0)


class Purchase(models.Model):
  
  menu_item = models.ForeignKey(MenuItem,on_delete=models.CASCADE)
  timestamp = models.DateTimeField(auto_now=True)


'''   def get_absolute_url(self):
        return "/purchases"
'''
  
