# Generated by Django 3.1.5 on 2021-02-01 13:27

import accounts.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0040_auto_20210131_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porder_useremail', models.EmailField(default=None, max_length=254)),
                ('porder_name', models.CharField(max_length=1024)),
                ('porder_price', models.PositiveIntegerField()),
                ('porder_publisher', models.CharField(max_length=1024)),
                ('porder_origin', models.CharField(max_length=1024)),
                ('porder_domain', models.CharField(default='null', max_length=100)),
                ('porder_phonenumber', models.IntegerField(default=9061325108)),
                ('ppaymentstatus', models.CharField(default=False, max_length=100)),
                ('porder_ordered_date', models.DateTimeField(default=datetime.datetime(2021, 2, 1, 18, 57, 52, 339463))),
                ('porder_delivery_date', models.DateTimeField(default=accounts.models.return_datetime)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='order_ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 1, 18, 57, 52, 339463)),
        ),
    ]