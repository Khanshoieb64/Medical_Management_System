from django.db import models
from datetime import date,datetime
# Create your models here.

# adding madicine
class AddMedicine(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    company=models.CharField(max_length=255)
    rate=models.IntegerField()
    mrp=models.IntegerField()
    quantity=models.IntegerField()
    type=models.CharField(max_length=255)
    purchase_date=models.DateField()
    expiry_date=models.DateField()
    

# signup model
class Register(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)

# login model
class LoginModel(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=255)
    password=models.CharField(max_length=255)