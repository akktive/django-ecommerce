from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

"""     Two steps:
        1. python manage.py makemigrations - to make a migration
        2. python manage.py migrate        - to apply changes
 """


class Category(models.Model):
    name = models.CharField(max_length=40)
    url = models.CharField(max_length=50, default="placeholder.png")

    def get_url(self):
        return reverse('category-url', args=[self.url])

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


# class Customer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)
#     email = models.EmailField()
#
#     def __str__(self):
#         return f'{self.user}'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    complete = models.BooleanField(default=False, null=True)

    def __str__(self):
        return f'{self.id}'

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
