# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    """
    This transforms a model instance to json and transforms a json to a model instance
    """
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    modifier = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Customer
        fields = ('id', 'name', 'surname', 'picture', 'owner', 'modifier')
