# Generated by Django 4.0.2 on 2022-02-26 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0003_remove_products_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Orders',
        ),
        migrations.DeleteModel(
            name='Products',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
