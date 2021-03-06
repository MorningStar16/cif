from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Region(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class Province(models.Model):
	region = models.ForeignKey(Region, on_delete=models.CASCADE)
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

class City(models.Model):
	province = models.ForeignKey(Province, on_delete=models.CASCADE)
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name


class Customer(models.Model):
	def upload_image(self, filename):
		return 'cif/docs/%s/%s' % (self.id, filename)

	created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	lastname = models.CharField(max_length=200)
	firstname = models.CharField(max_length=200)
	middlename = models.CharField(max_length=200, blank=True, null=True)
	birthday = models.CharField(max_length=200, blank=True, null=True)
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
	image1 = models.ImageField(upload_to=upload_image, blank=True, null=True)
	image2 = models.ImageField(upload_to=upload_image, blank=True, null=True)
	businesstype = models.CharField(max_length=200, blank=True, null=True)
	region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
	province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True, blank=True)
	city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)

	def save(self, *args, **kwargs):
		if self.id is None:
			saved_image1 = self.image1
			saved_image2 = self.image2
			self.image1 = None
			self.image2 = None
			super(Customer, self).save(*args, **kwargs)
			self.image1 = saved_image1
			self.image2 = saved_image2
			if 'force_insert' in kwargs:
				kwargs.pop('force_insert')
		super(Customer, self).save(*args, **kwargs)

	def __str__(self):
		return self.lastname
