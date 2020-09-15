# Generated by Django 3.0.8 on 2020-07-26 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='fenquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=254)),
                ('last_name', models.CharField(max_length=254)),
                ('phone_no', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField(max_length=254)),
                ('city', models.CharField(max_length=254)),
                ('state', models.CharField(max_length=254)),
                ('zipcode', models.IntegerField(max_length=254)),
                ('your_enquiry', models.TextField(max_length=254)),
            ],
        ),
    ]
