from django.db import models

# Create your models here.
class logform(models.Model):
    email=models.EmailField()
    passw=models.CharField(max_length=25)
   
    