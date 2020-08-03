from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Customer(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    lastname = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    middlename = models.CharField(max_length=200, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    homeaddress = models.TextField(blank=True, null=True)
    homeownership = models.CharField(max_length=200)
    phone = models.CharField(max_length=200, blank=True, null=True)
    businessname = models.CharField(max_length=200, blank=True, null=True)
    specialtypractice = models.CharField(max_length=200, blank=True, null=True)
    tenurepractice = models.CharField(max_length=200, blank=True, null=True)
    prcno = models.CharField(max_length=200, blank=True, null=True)
    businessaddress = models.TextField(blank=True, null=True)
    businessphone = models.CharField(max_length=200, blank=True, null=True)
    businessemail = models.CharField(max_length=200, blank=True, null=True)
    contactperson = models.CharField(max_length=200, blank=True, null=True)
    position = models.CharField(max_length=200, blank=True, null=True)
    contactpersonphone = models.CharField(max_length=200, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    sales_employee = models.CharField(max_length=200, default='Intercast')
    is_sap_encoded = models.BooleanField(default=False)

    def __str__(self):
        return self.lastname