from timezone_field import TimeZoneField
from django.db import models
import json
from django.http import HttpResponse


# Create your models here.
class Member(models.Model):
    id = models.CharField(max_length=60, primary_key=True)
    real_name = models.CharField(max_length=60)
    tz = TimeZoneField(default='America/Los_Angeles')


def __str__(self):
    return self.tz


class Period(models.Model):
    activity_periods = models.ForeignKey(Member, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()

