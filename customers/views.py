# -*- coding: utf-8 -*-
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Customer
from .serializers import CustomerSerializer


class ListCreateCustomerView(ListCreateAPIView):
    """
    This view accepts \n
    \t- POST REQUEST: to create a new customer\n
    - GET REQUEST: to list all existing customers\n
    """
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    def perform_create(self, serializer):
        serializer.save(modifier=self.request.user, owner=self.request.user)


class CustomerDetailView(RetrieveUpdateDestroyAPIView):
    """
    This view accepts the following request methods\n
    \t- GET: Fetches a single customer information\n
    - PUT: Full update of customer information\n
    - PATCH: Partial update of customer information\n
    - DELETE: Deletes a customer information
    """
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    def perform_update(self, serializer):
        serializer.save(modifier=self.request.user)
