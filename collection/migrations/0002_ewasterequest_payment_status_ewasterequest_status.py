# Generated by Django 4.2.5 on 2023-10-01 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("collection", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="ewasterequest",
            name="payment_status",
            field=models.CharField(
                choices=[("Unpaid", "Unpaid"), ("Paid", "Paid")],
                default="Unpaid",
                max_length=10,
            ),
        ),
        migrations.AddField(
            model_name="ewasterequest",
            name="status",
            field=models.CharField(
                choices=[
                    ("Pending", "Pending"),
                    ("Processing", "Processing"),
                    ("Completed", "Completed"),
                ],
                default="Pending",
                max_length=20,
            ),
        ),
    ]
