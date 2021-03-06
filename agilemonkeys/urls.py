# -*- coding: utf-8 -*-
"""agilemonkeys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from agilemonkeys import settings

schema_view = get_schema_view(
    openapi.Info(
        title='MiniCRM API',
        default_version='v1',
        description='',
        contact=openapi.Contact(email='abdulhakeemmustapha@gmail.com'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [path('admin/', admin.site.urls),
               path('auth/', include('djoser.urls')),
               path('auth/', include('djoser.urls.authtoken')),
               path('', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
               path('custom-auth/', include('authentication.urls')),
               path('customers/', include('customers.urls'))
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
