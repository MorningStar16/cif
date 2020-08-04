# Generated by Django 3.0.8 on 2020-08-04 01:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cif', '0011_auto_20200729_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='cif/images/'),
        ),
        migrations.AddField(
            model_name='customer',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='cif/images/'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
