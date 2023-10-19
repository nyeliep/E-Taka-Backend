# Generated by Django 4.2.1 on 2023-09-11 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='delivery',
            options={'verbose_name': 'Delivery', 'verbose_name_plural': 'Deliveries'},
        ),
        migrations.RemoveField(
            model_name='delivery',
            name='user',
        ),
        migrations.AlterField(
            model_name='delivery',
            name='delivery_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
