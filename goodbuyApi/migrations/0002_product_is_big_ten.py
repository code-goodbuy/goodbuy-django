# Generated by Django 2.2.7 on 2019-11-23 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goodbuyApi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_big_ten',
            field=models.BooleanField(default=False),
        ),
    ]
