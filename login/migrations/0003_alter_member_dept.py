# Generated by Django 3.2 on 2021-05-09 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20210501_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='dept',
            field=models.CharField(max_length=100),
        ),
    ]
