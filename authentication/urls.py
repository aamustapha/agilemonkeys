# -*- coding: utf-8 -*-
from django.urls import path

from .views import UpgradeView, DowngradeView
urlpatterns = [
    path('<int:id>/upgrade/', UpgradeView.as_view()),
    path('<int:id>/downgrade/', DowngradeView.as_view()),
]
