import datetime
import uuid

from django.db import models


# Create your models here.
from django.utils import timezone


class Client(models.Model):
    """Модель клиента."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=50, verbose_name='first name')
    last_name = models.CharField(max_length=50, verbose_name='last name')

    class Meta:
        verbose_name = 'Client'
        db_table = 'Client'
        ordering = ['last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Application(models.Model):
    """Модель заявки."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    type = models.ManyToManyField('ApplicationType', through='ApplicationWTypes')
    client = models.ForeignKey('Client', default=None, null=True, on_delete=models.CASCADE)
    short_description = models.TextField(max_length=400, verbose_name='short description', default='')
    pub_date = models.DateField(default=timezone.now)
    status = models.ForeignKey('ApplicationStatus', default=None, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Application'

    def __str__(self):
        return f'{self.pub_date} - {self.client} '


class ApplicationType(models.Model):
    """Модель типа заявки."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=50, verbose_name='type name')

    class Meta:
        verbose_name = 'ApplicationType'
        db_table = 'ApplicationType'
        ordering = ['name']

    def __str__(self):
        return self.name


class ApplicationWTypes(models.Model):
    """ M2M модель из типа заявки в заявку."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    application = models.ForeignKey('Application', default=None, null=True, on_delete=models.CASCADE)
    type = models.ForeignKey('ApplicationType', default=None, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'applications_with_types'
        unique_together = (('application', 'type'),)


class ApplicationStatus(models.Model):
    """Модель статуса заявки."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=50, verbose_name='type name')

    class Meta:
        verbose_name = 'ApplicationStatus'
        db_table = 'ApplicationStatus'
        ordering = ['name']

    def __str__(self):
        return self.name


