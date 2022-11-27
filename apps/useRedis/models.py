from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=125)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

class CarDetail(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name