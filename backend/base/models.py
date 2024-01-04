from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='product_images/')
    brand = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()
    ratings = models.DecimalField(max_digits=3, decimal_places=1)
    numReviews = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    countInStock = models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True)

    def __str__(self):
           return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50)
    tax_price = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField(null=True, blank=True)
    is_delivered = models.BooleanField(default=False)
    delivered_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='order_item_images/')
    _id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name

class ShippingAddress(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    shipping_price = models.DecimalField(max_digits=10, decimal_places=2)
    _id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name