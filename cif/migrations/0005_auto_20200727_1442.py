# Generated by Django 3.0.8 on 2020-07-27 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cif', '0004_auto_20200727_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]
