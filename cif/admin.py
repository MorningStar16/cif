from django.contrib import admin
from . models import Customer, Region, Province, City

admin.site.register(Customer)
admin.site.register(Region)
admin.site.register(Province)
admin.site.register(City)
