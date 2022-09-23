from http.cookies import BaseCookie
from django.db import models


# Create your models here.
class regform(models.Model):
    book=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    disc=models.CharField(max_length=50)
    price=models.IntegerField()
    def __str__(self):
        return self.book