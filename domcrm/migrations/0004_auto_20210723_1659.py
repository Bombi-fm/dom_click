# Generated by Django 3.2.5 on 2021-07-23 13:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domcrm', '0003_auto_20210723_1654'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={'verbose_name': 'Application'},
        ),
        migrations.AlterField(
            model_name='application',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 23, 16, 59, 44, 838978)),
        ),
    ]
