# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Result(models.Model):
    period = models.TextField()
    ratio = models.TextField()


class Rest(models.Model):
    title = models.CharField(max_length=20)
    keyword = models.CharField(max_length=20)
    start_date = models.CharField(max_length=12)
    end_date = models.CharField(max_length=12)
    result = models.ForeignKey(Result)
