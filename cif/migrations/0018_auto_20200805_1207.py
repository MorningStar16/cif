# Generated by Django 3.0.8 on 2020-08-05 04:07

import cif.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cif', '0017_delete_gallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to=cif.models.Customer.upload_image),
        ),
        migrations.AlterField(
            model_name='customer',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to=cif.models.Customer.upload_image),
        ),
    ]