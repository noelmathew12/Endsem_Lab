from django.db import models

# Create your models here.

CITIES=(
    ('mumbai', 'MUMBAI'),
    ('delhi','DELHI'),
    ('bangalore', 'BANGALORE'),
    ('chennai', 'CHENNAI'),
    ('kolkata', 'KOLKATA'),
)

class BookingItems(models.Model):
    content = models.TextField()
    user= models.CharField(max_length=100) 

class Mymodel(models.Model):
    travelling_from= models.CharField(max_length=9, choices=CITIES, default= 'delhi')
    travelling_to= models.CharField(max_length=9, choices=CITIES, default= 'mumbai')
    date_of_travelling=models.DateField(default='07-12-2022')
    number_of_passengers=models.IntegerField(max_length=2)
    def __str__(self):
        return f"{self.number_of_passengers}"

