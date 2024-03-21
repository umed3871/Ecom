from django.db import models

# Create your models here.

class Registration(models.Model):
    first_name = models.CharField(max_length=100, default='', null=True)
    last_name = models.CharField(max_length=100, default='', null=True)
    mobile = models.IntegerField(default=1)
    email = models.CharField(max_length=100, default='', null=True)
    password = models.CharField(max_length=100, default='', null=True)
    gender = models.CharField(max_length=100, default='', null=True)
    
    def __str__(self):
        return self.first_name
    
class Category(models.Model):
    category_image = models.ImageField(upload_to="uploads/category/")
    category_name = models.CharField(max_length=100, default='', null=True)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=100, default='', null=True)
    product_image = models.ImageField(upload_to="uploads/product/")
    product_desc = models.CharField(max_length=300, default='', null=True)
    product_price = models.IntegerField(default=1)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.product_name