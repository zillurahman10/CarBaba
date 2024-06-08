from brand import models as brandModel
from django.db import models
# Create your models here.
class Car(models.Model):
    car_name = models.CharField(max_length=100)
    price = models.IntegerField(blank="True", null="True")
    image = models.ImageField(upload_to="car/uploads/")
    quantity = models.IntegerField(blank="True", null="True")
    description = models.TextField()
    brand = models.ForeignKey(brandModel.Brand, on_delete=models.CASCADE, blank="True", null="True")

    def __str__(self):
        return self.car_name

class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name