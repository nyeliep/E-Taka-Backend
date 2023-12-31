# Generated by Django 4.2.1 on 2023-09-11 07:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0002_alter_delivery_options_remove_delivery_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='customer_name',
            field=models.CharField(default='Default Customer', max_length=100),
        ),
        migrations.AddField(
            model_name='delivery',
            name='delivery_address',
            field=models.CharField(default='Default Address', max_length=200),
        ),
        migrations.AddField(
            model_name='delivery',
            name='delivery_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='delivery',
            name='delivery_status',
            field=models.CharField(default='Pending', max_length=50),
        ),
        migrations.AddField(
            model_name='delivery',
            name='product_name',
            field=models.CharField(default='Default Product', max_length=100),
        ),
    ]
