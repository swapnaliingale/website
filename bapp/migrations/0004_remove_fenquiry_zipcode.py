# Generated by Django 3.0.8 on 2020-07-27 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bapp', '0003_auto_20200726_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fenquiry',
            name='zipcode',
        ),
    ]
