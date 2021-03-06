# Generated by Django 3.2.8 on 2021-10-09 01:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('productType', models.CharField(choices=[('eletronic', 'Eletronic'), ('home_appliances', 'Home Appliances'), ('mobile', 'Mobile')], max_length=255)),
                ('sale_value', models.FloatField()),
                ('stock_quantity', models.IntegerField()),
            ],
        ),
    ]
