from django.db import models
from django.contrib.auth.models import User
from car.models import Car

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.OneToOneField(Car, on_delete=models.CASCADE)
    bought_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    