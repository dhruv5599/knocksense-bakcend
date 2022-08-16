from email.policy import default
from django.db import models
# from django.contrib.postgres.fields import ArrayField
from django_mysql.models import ListCharField


# Create your models here.
class News(models.Model):
    headline            = models.CharField(max_length=255, null=False, blank=False)
    subheadline         = models.CharField(max_length=255, null=False, blank=False)
    image               = models.ImageField(upload_to='images/',null = False, blank =True)   #image feilds
    mianbody            = models.CharField(max_length=255, null=False, blank=False)
    tag                 = ListCharField(base_field=models.IntegerField(), size=5, max_length=(5 * 257))
    timepost            = models.DateTimeField(auto_now_add=True)
    author              = models.PositiveIntegerField() \
        # from user table (dhruv's id = 5)
    category            = models.PositiveIntegerField()  \
        # amdin
        # from category table (sports =1 , it =-2)
    locality            = models.PositiveIntegerField()  \
        # amdin
        # from locality table (new-mumbai = 1 , sahibagh = 2)
    city                = models.PositiveIntegerField()  \
        # amdin
        # from city table (ahmedabad = 1 , lucknow = 2) 
    is_activate = models.BooleanField(default=True) 
    modified_date       = models.DateTimeField(auto_now=True)
    
    
    def __str__(self) -> str:
        return f"{self.pk} -> {self.headline}"
    
    
class Category(models.Model):
    # id is default
    category            = models.CharField(max_length=255) \
        # from category table (knock-out = 1 , health&wellness = 2)\

    def __str__(self) -> str:
        return f"{self.category} -> {self.id}"
    
class Locality(models.Model):
    # id is default
    locality            = models.CharField(max_length=255)  \
        # from locality table (new-mumbai = 1 , sahibagh = 2)
    
    def __str__(self) -> str:
        return f"{self.locality} -> {self.id}"
    
class City(models.Model):
     # id is default
    city                = models.CharField(max_length=255) \
        # from city table (ahmedabad = 1 , udaipur = 2)
    
    def __str__(self) -> str:
        return f"{self.city} -> {self.id}"
    
    
class Tag(models.Model):
    # id is default
    tag                = models.CharField(max_length=255)  
    
    def __str__(self) -> str:
        return f"{self.id} --> {self.tag}"
    
    

    
class Comment(models.Model):                    
    # this id is come from news table
    comment         = models.CharField(max_length=255)
    comment_news    = models.IntegerField(default=0)    \
        # news pk // which news
    user            = models.IntegerField(default=0)    \
        # user pk
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField( auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.comment}"
    
class Like(models.Model):
    # change like field in bollen /// because like nd dislike
    # // nd how many like in this news so we can count all ture value
    like            = models.PositiveIntegerField()
    user            = models.IntegerField(default=0)  \
        # user pk
    like_news       = models.IntegerField(default=0)   \
        # news pk
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField( auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.user}"