# Generated by Django 3.0.8 on 2020-07-27 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bapp', '0005_remove_fenquiry_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fenquiry',
            old_name='city',
            new_name='city_name',
        ),
        migrations.RenameField(
            model_name='fenquiry',
            old_name='email',
            new_name='email_Id',
        ),
        migrations.RenameField(
            model_name='fenquiry',
            old_name='state',
            new_name='state_name',
        ),
    ]