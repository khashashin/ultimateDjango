from django.contrib import admin
from django.urls import path, re_path
from .views import AccountList

urlpatterns = [
    re_path(r'^$',
        AccountList.account_detail, name='account_detail'
    ),
]
