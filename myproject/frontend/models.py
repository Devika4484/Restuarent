from django.db import models

# Create your models here.
class login(models.Model):
    Name = models.CharField(max_length=30, null=True, blank=True)
    Lname = models.CharField(max_length=30, null=True, blank=True)
    Uname = models.CharField(max_length=30, null=True, blank=True)
    Email = models.CharField(max_length=30,null=True, blank=True)
    Password = models.CharField(max_length=30,null=True, blank=True)
    Cpassword= models.CharField(max_length=30,null=True, blank=True)

                        #Booking

class booking(models.Model):
    Name = models.CharField(max_length=30, null=True, blank=True)
    Phone = models.CharField(max_length=30, null=True, blank=True)
    Email = models.CharField(max_length=30,null=True, blank=True)
    NPersons = models.IntegerField(null=True, blank=True)
    Date = models.DateTimeField(null=True, blank=True)

                        #contact

class contact(models.Model):
    Name = models.CharField(max_length=30, null=True, blank=True)
    Email = models.CharField(max_length=50, null=True, blank=True)
    Subject = models.CharField(max_length=50, null=True, blank=True)
    Message = models.CharField(max_length=300,null=True, blank=True)

                        #Billing

class billing(models.Model):
    Fname = models.CharField(max_length=30, null=True, blank=True)
    Lname = models.CharField(max_length=30, null=True, blank=True)
    Uname = models.CharField(max_length=30, null=True, blank=True)
    Email = models.CharField(max_length=30, null=True, blank=True)
    Address = models.CharField(max_length=200, null=True, blank=True)
