# Generated by Django 4.2.5 on 2023-09-18 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_options_remove_order_order_id_and_more'),
        ('delivery', '0019_delivery_customer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='delivery', to='order.order'),
            preserve_default=False,
        ),
    ]