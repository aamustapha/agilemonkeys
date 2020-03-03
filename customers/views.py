# -*- coding: utf-8 -*-
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Customer
from .serializers import CustomerSerializer


class ListCreateCustomerView(ListCreateAPIView):
    """
    This view accepts
    -> POST REQUEST: to create a new customer
    -> GET REQUEST: to list all existing customers
    """
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    def perform_create(self, serializer):
        serializer.save(modifier=self.request.user, owner=self.request.user)


class CustomerDetailView(RetrieveUpdateDestroyAPIView):
    """
    This view accepts the following request methods
    -> GET: Fetches a single customer information
    -> PUT: Full update of customer information
    -> PATCH: Partial update of customer information
    -> DELETE: Deletes a customer information
    """
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    def perform_update(self, serializer):
        serializer.save(modifier=self.request.user)
