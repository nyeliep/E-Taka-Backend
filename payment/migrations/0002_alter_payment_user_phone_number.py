# Generated by Django 4.2.5 on 2023-10-12 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payment", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="user_phone_number",
            field=models.CharField(max_length=14),
        ),
    ]