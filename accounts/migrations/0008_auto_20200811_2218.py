# Generated by Django 3.0.8 on 2020-08-11 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200811_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addtocart',
            name='cart_image',
            field=models.ImageField(upload_to='cart/'),
        ),
    ]
