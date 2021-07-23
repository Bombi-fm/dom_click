# Generated by Django 3.2.5 on 2021-07-22 19:47

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('short_description', models.CharField(default='', max_length=400, verbose_name='short description')),
                ('pub_date', models.DateField(default=datetime.date(2000, 1, 1))),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50, verbose_name='type name')),
            ],
            options={
                'verbose_name': 'ApplicationType',
                'db_table': 'ApplicationType',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=50, verbose_name='first name')),
                ('last_name', models.CharField(max_length=50, verbose_name='last name')),
            ],
            options={
                'verbose_name': 'Client',
                'db_table': 'Client',
                'ordering': ['last_name'],
            },
        ),
        migrations.CreateModel(
            name='ApplicationWTypes',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('application', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='domcrm.application')),
                ('type', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='domcrm.applicationtype')),
            ],
            options={
                'db_table': 'applications_with_types',
                'unique_together': {('application', 'type')},
            },
        ),
        migrations.AddField(
            model_name='application',
            name='client',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='domcrm.client'),
        ),
        migrations.AddField(
            model_name='application',
            name='type',
            field=models.ManyToManyField(through='domcrm.ApplicationWTypes', to='domcrm.ApplicationType'),
        ),
    ]