# Generated by Django 4.2.1 on 2023-09-12 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0009_remove_delivery_delivery_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='product_name',
        ),
    ]
