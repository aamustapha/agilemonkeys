# -*- coding: utf-8 -*-
from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    picture = models.ImageField(blank=True, null=True)
