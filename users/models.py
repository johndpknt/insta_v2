# Create your models here.

from django.db import models
import uuid
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField


class Users(models.Model):
    USER_TYPES = [('ADMIN','admin'), ('REGULAR','regular')]
    first_name = models.CharField(max_length=60, null=True, blank=False)
    last_name = models.CharField(max_length=60, null=True, blank=False)
    email = models.EmailField(max_length=60, null=True, blank=False)
    phone_number = PhoneNumberField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=60, choices=USER_TYPES, null=False, default = 'admin')
    updated_date = models.DateTimeField(null=True, blank=True) 


    def save(self, *args, **kwargs):
        self.updated_date = datetime.now()
        return super(Users, self).save(*args, **kwargs)

    def __str__(self):
        return "{} - {}".format(first_name, last_name)

    class Meta:
        db_table = "users"
