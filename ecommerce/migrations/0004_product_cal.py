# Generated by Django 4.2.2 on 2023-06-29 03:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_alter_car_options_car_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cal',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Calificacion'),
        ),
    ]
