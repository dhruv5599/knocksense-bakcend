from time import time
from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class User(models.Model):
    # do not touch
    phone_number = PhoneNumberField(unique=True)
    address = models.CharField(max_length=255, blank=True, null= True)
    professional_email = models.EmailField(blank=True, null= True, unique= True)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1) # This entry should be only 'M' & 'F' to be checked in serailizer
    email = models.EmailField(blank=True, null= True)
    firstname = models.CharField( max_length=150, blank=True, null= True)
    lastname = models.CharField( max_length=150, blank=True, null= True)
    username = models.CharField(max_length = 255, unique = True)
    is_author = models.BooleanField(default=False)
    is_activate = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.firstname} - {self.id}"