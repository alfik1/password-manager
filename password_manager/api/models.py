from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Password(models.Model): 
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="p_user")
    email = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    password = models.CharField(max_length=8)

    def __str__(self) -> str:
        return self.user


