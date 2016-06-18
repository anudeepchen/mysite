from __future__ import unicode_literals
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from djangotoolbox.fields import ListField
# Create your models here.

class User_Profile(models.Model):
    user  = ListField(models.OneToOneField(User,primary_key=True))
    email = models.EmailField(null=False, blank=False, default="", unique = True)
    location=models.CharField(max_length=120,null=False,default="")
    phone_regex = RegexValidator(regex=r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$')
    phone = models.CharField(max_length=15, validators=[phone_regex], null = False, blank=False, default="")
    promo_code = models.CharField(max_length=15, null = False, blank=False, default="")
    
    
    def _str_(self):
        return self.email
