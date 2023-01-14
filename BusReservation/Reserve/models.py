from django.db import models

# Create your models here.
class Driver(models.Model):
    name=models.CharField(max_length=35)
    age=models.PositiveIntegerField()

    def __str__(self):
        return self.name



class Bus(models.Model):
    bus_name = models.CharField(max_length=30)
    bus_number=models.IntegerField()
    driver=models.ForeignKey(Driver,on_delete=models.CASCADE)
    seat_list=models.IntegerField(default=10)
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30)
    entiryhour = models.DecimalField(decimal_places=0, max_digits=2)
    entirymin = models.DecimalField(decimal_places=0, max_digits=2)
    exithour = models.DecimalField(decimal_places=0, max_digits=2)
    exitmin = models.DecimalField(decimal_places=0, max_digits=2)
    seat_num=models.IntegerField(blank=True,null=True)
    seat_num_available=models.BooleanField(default=True,blank=True,null=True)

    def __str__(self):
        return self.bus_name

