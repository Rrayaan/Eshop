from email.policy import default
from django.db import models
import datetime

# Create your models here.


class signup(models.Model):
    firstname = models.CharField(max_length=100, default="")
    lastname = models.CharField(max_length=100, default="")
    email = models.CharField(max_length=100, default="")
    password = models.CharField(max_length=100, default="")
    gender = models.CharField(max_length=100, default="")
    mobile = models.BigIntegerField()

    def __str__(self):
        return self.firstname


class category(models.Model):
    name = models.CharField(max_length=100, default="")
    category_img = models.ImageField(upload_to='upload/', null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_name = models.CharField(max_length=100, default="")
    price = models.IntegerField()
    desc = models.TextField(max_length=100, null=True)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='upload/product/', null=True)

    def __str__(self):
        return self.product_name


class order_dtls(models.Model):
    address = models.CharField(max_length=200)
    mobile = models.BigIntegerField()
    customer = models.ForeignKey(signup, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    date = models.DateTimeField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product.product_name
