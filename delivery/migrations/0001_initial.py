# Generated by Django 4.2.1 on 2023-09-08 12:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_time', models.DateTimeField()),
                ('delivery_unit', models.CharField(choices=[('mins', 'Minutes'), ('hrs', 'Hours')], default='mins', max_length=4)),
                ('delivery_method', models.CharField(choices=[('pickup', 'Pickup'), ('home delivery', 'Home Delivery')], default='Pickup', max_length=20)),
                ('status', models.CharField(max_length=26)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Delivery',
                'verbose_name_plural': 'Delivery',
                'db_table': 'Delivery',
            },
        ),
    ]