# Generated by Django 4.2.3 on 2023-10-18 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_price_date_price_last_name_price_name_price_year'),
    ]

    operations = [
        migrations.RenameField(
            model_name='price',
            old_name='date',
            new_name='data',
        ),
    ]
