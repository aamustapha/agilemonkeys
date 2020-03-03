# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    """
    This transforms a model instance to json and transforms a json to a model instance
    """
    class Meta:
        model = Customer
        fields = ('name', 'surname', 'picture')
