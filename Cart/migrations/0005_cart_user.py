# Generated by Django 4.2.5 on 2023-10-17 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("useraccount", "0005_alter_useraccount_confirm_password"),
        ("Cart", "0004_remove_cart_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="useraccount.useraccount",
            ),
        ),
    ]
