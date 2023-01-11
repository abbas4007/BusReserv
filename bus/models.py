from django.db import models

# Create your models here.
class Driver(models.Model):
    name=models.CharField(max_length=30)
    age=models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Bus(models.Model):
    bus_name=models.CharField(max_length=35)
    driver=models.ForeignKey(Driver,on_delete=models.CASCADE)
    seat_count=models.IntegerField(default=15)
    # seat_number=models.IntegerField()
    seat_empty=models.BooleanField(default=True)
    entiry=models.TimeField(auto_now_add=True)
    exit=models.TimeField(auto_now=True)

    def __str__(self):
        return self.bus_name