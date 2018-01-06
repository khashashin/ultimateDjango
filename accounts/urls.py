from django.contrib import admin
from django.urls import path, re_path
from .views import account_detail, account_cru

urlpatterns = [
    re_path(r'^$', account_detail, name='account_detail'),
    re_path(r'^edit/$', account_cru, name='account_update'),
]
