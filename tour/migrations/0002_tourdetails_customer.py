# Generated by Django 5.0.2 on 2024-02-09 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminsection', '0001_initial'),
        ('tour', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourdetails',
            name='customer',
            field=models.ManyToManyField(to='adminsection.customerdetails'),
        ),
    ]
