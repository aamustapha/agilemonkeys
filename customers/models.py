# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    picture = models.ImageField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    modifier = models.ForeignKey(User, on_delete=models.CASCADE, related_name='modifier')
