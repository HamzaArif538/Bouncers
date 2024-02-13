from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.IntegerField(null=True)
    oldprice = models.IntegerField(null=True)
    color = models.CharField(max_length=50, null=True)
    picture = models.ImageField(upload_to='product_images/', null=True, blank=True)
    CATEGORY = (
        ('Formal Shoes', 'Formal Shoes'),
        ('Peshawari', 'Peshawari')
    )
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    AVAILABILITY = (
        ('In Stock', 'In Stock'),
        ('Out of Stock', 'Out of Stock')
    )
    availability = models.CharField(max_length=200, null=True, choices=AVAILABILITY)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return self.name


