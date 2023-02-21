from django.db import models

# Create your models here.
class staffdb(models.Model):
    Name = models.CharField(max_length=30, null=True, blank=True)
    Email = models.CharField(max_length=30,null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Username = models.CharField(max_length=30,null=True, blank=True)
    Password =  models.CharField(max_length=30,null=True, blank=True)
    Confirm_Password = models.CharField(max_length=30, null=True, blank=True)
    Image = models.ImageField(upload_to="Profile", null=True, blank=True)


                           #Loginpage
class user(models.Model):
    username = models.CharField(max_length=30, null=True, blank=True)
    password = models.CharField(max_length=30, null=True, blank=True)
    email = models.CharField(max_length=30, null=True, blank=True)

                          #Category

class cdb(models.Model):
        Category_Name = models.CharField(max_length=30, null=True, blank=True)
        Description = models.CharField(max_length=30, null=True, blank=True)
        Image = models.ImageField(upload_to="Profile", null=True, blank=True)

                        #products

class pdb(models.Model):
        Category_Name = models.CharField(max_length=30, null=True, blank=True)
        Product_Name = models.CharField(max_length=30, null=True, blank=True)
        Product_Price = models.IntegerField(null=True, blank=True)
        Quantity = models.IntegerField(null=True, blank=True)
        Image = models.ImageField(upload_to="Profile", null=True, blank=True)

