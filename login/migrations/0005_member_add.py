# Generated by Django 3.2 on 2021-05-10 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_member_profile_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='add',
            field=models.CharField(max_length=100, null=True),
        ),
    ]