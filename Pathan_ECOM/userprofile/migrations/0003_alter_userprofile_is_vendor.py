# Generated by Django 4.2.11 on 2024-03-25 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_userprofile_is_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='is_vendor',
            field=models.BooleanField(blank=True),
        ),
    ]
