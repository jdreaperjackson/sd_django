# Generated by Django 3.2.7 on 2022-07-10 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sd_app', '0010_alter_userprofile_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='zip_code',
            field=models.CharField(blank=True, max_length=9),
        ),
    ]
