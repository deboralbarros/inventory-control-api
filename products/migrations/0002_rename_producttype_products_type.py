# Generated by Django 3.2.8 on 2021-10-09 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='productType',
            new_name='type',
        ),
    ]