# Generated by Django 3.0.8 on 2020-08-13 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_userregister_user_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregister',
            name='user_address',
            field=models.TextField(default=None),
        ),
    ]
