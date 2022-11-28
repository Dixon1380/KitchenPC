from django.db import models

# Create your models here.


#More stores will be added soon.
STORES = {
    'Amazon':'',
    'Kroger':'',
    'Target':'',
    'Walmart':'',
}


class PriceChecker(models.Model):
    item_name = models.CharField(max_length=150)
    item_price = models.DecimalField(decimal_places=2, max_digits=10)
    item_location=models.CharField(max_length=50)
    item_availability = models.BooleanField()
    item_quantity = models.IntegerField()
