from django.db import models

# Create your models here.


class Device(models.Model):

    type = models.CharField(max_length=100)
    price = models.IntegerField()

    choices = (
        ('AVAILABLE', 'Item ready'),
        ('SOLD', 'sold'),
        ('RESTOCKING', 'restocking')
    )

    status = models.CharField(max_length=10, choices=choices, default='SOLD')
    issues = models.CharField(max_length=50, default="No Issues")

    class Meta:
        abstract = True

    def __str__(self):
        return  'Type: {0} Price: {1}'.format(self.type, self.price)


class Desktops(Device):
    pass


class Laptops(Device):
    pass


class Mobiles(Device):
    pass

