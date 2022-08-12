from django.contrib import admin
from .models import News, Category, Locality, City, Comment, Like, Tag

# Register your models here.

admin.site.register([News, Category, Locality, City, Comment, Like, Tag])