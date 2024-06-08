from django.db import models
# from car.models import Car
# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=500, unique=True, null=True)
    def __str__(self) -> str:
        return self.name
    