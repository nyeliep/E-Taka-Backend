# Generated by Django 4.2.1 on 2023-09-11 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0007_delivery_delivery_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='delivery_date',
        ),
    ]
