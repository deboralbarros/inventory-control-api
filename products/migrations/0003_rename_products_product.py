# Generated by Django 3.2.8 on 2021-10-09 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_producttype_products_type'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]
