# Generated by Django 4.0.2 on 2022-02-26 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0005_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='owner',
        ),
    ]
