# Generated by Django 3.0.8 on 2020-07-27 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bapp', '0004_remove_fenquiry_zipcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fenquiry',
            name='address',
        ),
    ]
