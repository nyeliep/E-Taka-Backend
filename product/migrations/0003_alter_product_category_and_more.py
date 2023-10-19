# Generated by Django 4.2.5 on 2023-09-13 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_remove_product_id_product_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('television', 'Television'), ('fridges', 'Fridges'), ('phones', 'Phones'), ('cables', 'Cables'), ('woofers', 'Woofers'), ('radio', 'Radio'), ('laptops', 'Laptops'), ('microwave', 'Microwave')], max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity_of_items',
            field=models.PositiveIntegerField(),
        ),
    ]