from django.contrib import admin
from django.urls import path, re_path
from .views import account_detail

urlpatterns = [
    re_path(r'^$', account_detail, name='account_detail'),
]
