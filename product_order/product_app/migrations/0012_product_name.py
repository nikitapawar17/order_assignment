# Generated by Django 4.0.2 on 2022-02-27 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0011_product_ordered_quantity_product_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
