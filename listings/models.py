from django.db import models
from datetime import datetime
from realtors.models import Realtor

class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    adderss = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    sqft = models.IntegerField()
    offers = models.CharField(max_length=8, help_text = 'enter Discount Percentage as 10% off')
    photo_main = models.ImageField(upload_to='Photos/%Y/%M/%D')
    photo_1 = models.ImageField(upload_to='Photos/%Y/%M/%D', blank=True)
    photo_2 = models.ImageField(upload_to='Photos/%Y/%M/%D', blank=True)
    photo_3 = models.ImageField(upload_to='Photos/%Y/%M/%D', blank=True)
    photo_4 = models.ImageField(upload_to='Photos/%Y/%M/%D', blank=True)
    photo_5 = models.ImageField(upload_to='Photos/%Y/%M/%D', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    apt_types = (
    ('Apartments', 'Apartment'),
    ('Lands', 'Land'),
    ('villas','Villa'),
    ('Bars', 'Bar'),
    ('Stores', 'Store'),
    ('Farms', 'Farm')
    )

    types = models.CharField(
    max_length= 10,
    choices = apt_types,
    default = 'Apartments',
    blank = False
    )

    def __str__(self):
        return f'{self.title}'
