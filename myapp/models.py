from django.db import models

# Create your models here.
class Users(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    
    def __str__(self):
        return self.fname +' '+ self.lname    
    
class Donation(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    door_number = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    FOOD_CHOICES = [
        ('veg', 'Vegetarian'),
        ('nonveg', 'Non-Vegetarian'),
    ]
    food_type = models.CharField(max_length=10, choices=FOOD_CHOICES)
    food_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    phone_number = models.CharField(max_length=15)

class Order(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    food_id= models.IntegerField()
    door_number = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    quantity = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    