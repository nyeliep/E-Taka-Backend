# Generated by Django 4.2.1 on 2023-09-12 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0011_alter_delivery_delivery_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='delivery_unit',
            field=models.CharField(choices=[('mins', 'Minutes'), ('hrs', 'Hours')], default='mins', max_length=4),
        ),
    ]