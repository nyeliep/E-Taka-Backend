
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0010_remove_delivery_product_name'),
    ]

    DELIVERY_TIME_OPTIONS = [
        ('mins', 'Minutes'),
        ('hours', 'Hours'),
        ('days', 'Days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='delivery_unit',
            field=models.CharField(max_length=4, choices=DELIVERY_TIME_OPTIONS, default='mins'),
        ),
    ]

   
