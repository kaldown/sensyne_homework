from django.db import models


class Product(models.Model):
    # 1. better use in separate table
    # 2. better use dataclass
    CURRENCIES = [
        ('GBP', 'Pound'),
    ]
    product_code = models.CharField(max_length=16)
    product_name = models.CharField(max_length=256)
    price = models.PositiveIntegerField()
    currency = models.CharField(max_length=256, choices=CURRENCIES)

    def __str__(self):
        return f"{self.product_name}"
