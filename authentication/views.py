# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView


class UpgradeView(APIView):
    """Method to set user admin status"""
    permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=kwargs.get('id'))
            user.is_staff = True
            user.save()
            return JsonResponse({'status': True})
        except User.DoesNotExist:
            return JsonResponse({'status': False}, status=404)


class DowngradeView(APIView):
    """Method to unset user admin status"""
    permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=kwargs.get('id'))
            user.is_staff = False
            user.save()
            return JsonResponse({'status': True})
        except User.DoesNotExist:
            return JsonResponse({'status': False}, status=404)
