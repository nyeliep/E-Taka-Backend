# Generated by Django 4.2.1 on 2023-09-14 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0018_alter_delivery_delivery_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='customer_name',
            field=models.CharField(default='customer', max_length=100),
        ),
    ]