from django.db import models

# Create your models here.

class Register(models.Model):
    Name = models.CharField(max_length=220, default="")
    Email = models.EmailField(unique="True")
    Password =models.CharField(max_length=220, default="")