# Generated by Django 3.2.5 on 2021-07-23 13:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('domcrm', '0002_auto_20210723_1652'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='staus',
        ),
        migrations.AddField(
            model_name='application',
            name='status',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='domcrm.applicationstatus'),
        ),
        migrations.AlterField(
            model_name='application',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2021, 7, 23, 16, 54, 49, 708904)),
        ),
    ]
