# Generated by Django 5.0.2 on 2024-02-09 09:26

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Gender', models.CharField(max_length=50)),
                ('Phone_No', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('Address', models.CharField(max_length=500)),
                ('Aadhaar_No', models.BigIntegerField()),
            ],
            options={
                'db_table': 'SLT_CUSTOMER_DETAILS',
            },
        ),
        migrations.CreateModel(
            name='TrainDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Train_No', models.IntegerField()),
                ('Journey_Date', models.DateField()),
            ],
            options={
                'db_table': 'SLT_TOURS_TRAIN_DETAILS',
            },
        ),
    ]
