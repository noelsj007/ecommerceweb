# Generated by Django 3.1.5 on 2021-02-03 04:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0051_auto_20210203_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 3, 10, 13, 2, 734734)),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_blog',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_event',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_login',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_news',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 3, 10, 13, 2, 734734)),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_product',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_shop',
            field=models.CharField(max_length=100),
        ),
    ]