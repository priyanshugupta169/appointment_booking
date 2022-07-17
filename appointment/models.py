from django.db import models
from datetime import date
from django.db.models import Max
import json
import re
# from django.contrib.postgres.fields import JSONField
# from jsonfield import JSONField

# from django.contrib.auth.base_user import BaseUserManager,AbstractBaseUser

# Create your models here.
class Preacher(models.Model):
    TYPE = (
        ('SK'),('SR'),('PA'),
        ('ESK'),('BSK'),('BPA')
    )
    id=models.CharField(max_length=20,editable=False,primary_key=True)
    email=models.EmailField(max_length=100,blank=True)
    name=models.CharField(max_length=100)
    availability_dates=models.JSONField(blank=True)
    contact_info=models.CharField(max_length=70)
    type=models.JSONField(blank=True)
    # type=models.CharField(max_length=70,choices=TYPE)
    creation_date = models.DateField(default=date.today)

    def save(self, force_insert=True, **kwargs):
        if not self.id or self.id==None:
            max = Preacher.objects.aggregate(id_max=Max('id'))['id_max']
            max = re.search(r'\d+', max)
            print(int(max.group(0)))
            print(self.name)
            self.id = "{}{:06d}".format('PR_', int(max.group(0))+1 if max is not None else 1)
            print(self.id)
        super().save(*kwargs)


class Location(models.Model):
    id=models.CharField(max_length=20,editable=False,primary_key=True)
    name=models.CharField(max_length=100)
    creation_date = models.DateField(default=date.today)

    def save(self, **kwargs):
        if not self.id:
            max = Location.objects.aggregate(id_max=Max('id'))['id_max']
            max = re.search(r'\d+', max)
            self.id = "{}{:04d}".format('CT_', int(max.group(0))+1 if max is not None else 1)
        super().save(*kwargs)

class Topic(models.Model):
    id=models.CharField(max_length=20,primary_key=True, editable=False)
    name=models.CharField(max_length=100)
    type=models.JSONField(blank=True)
    creation_date = models.DateField(default=date.today)

    def save(self, **kwargs):
        if not self.id:
            max = Topic.objects.aggregate(id_max=Max('id'))['id_max']
            max = re.search(r'\d+', max)
            self.id = "{}{:04d}".format('TP_', int(max.group(0))+1 if max is not None else 1)
        super().save(*kwargs)


class Appointment(models.Model):
    id=models.CharField(max_length=20,primary_key=True, editable=False)
    schedule_id=models.CharField(max_length=100)
    appointment_date=models.CharField(max_length=70)
    month=models.CharField(max_length=70)
    preacher_id=models.CharField(max_length=70)
    topic_id=models.CharField(max_length=70)
    location_id=models.CharField(max_length=70)
    creation_date = models.DateField(default=date.today)

    def save(self, **kwargs):
        if not self.id:
            max = Appointment.objects.aggregate(id_max=Max('id'))['id_max']
            max = re.search(r'\d+', max)
            self.id = "{}{:08d}".format('AP_', int(max.group(0))+1 if max is not None else 1)
        super().save(*kwargs)