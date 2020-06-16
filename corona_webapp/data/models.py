from django.db import models
from datetime import date




class Ventilator(models.Model):
    s_no=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,default=False)
    total=models.IntegerField(default=100)
    available=models.IntegerField(default=100)
    date = models.DateField(default=date.today)

    def __str__(self):
        return str(self.date)

class Bed(models.Model):
    total=models.IntegerField(default=200)
    name=models.CharField(max_length=100,default=False)
    available=models.IntegerField(default=100)
    date = models.DateField(default=date.today)

    def __str__(self):
        return str(self.date)

class Hospital(models.Model):
    hospitals=models.CharField(max_length=50)
    nodoctor=models.IntegerField(default=20)
    nonurse=models.IntegerField(default=30)
    date = models.DateField(default=date.today)

    def __str__(self):
        return str(self.date)

class Patient(models.Model):
    total=models.IntegerField(default=200)
    recovered=models.IntegerField(default=20)
    positive=models.IntegerField(default=180)
    death=models.IntegerField(default=2)
    date = models.DateField(default=date.today)

    def __str__(self):
        return str(self.date)




    

   

    


# Create your models here.
