# Generated by Django 3.2.7 on 2022-07-10 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sd_app', '0021_auto_20220710_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='delivery_address',
            field=models.CharField(default='ADDRESS IN PROFILE', max_length=35),
        ),
    ]
