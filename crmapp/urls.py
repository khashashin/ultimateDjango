"""crmapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path, include
from marketing import views as marketing_views
from subscribers import views as subscr_views
from django.contrib.auth import views as django_views
from accounts.views import AccountList as account_views
from accounts.views import account_cru
from contacts.views import contact_cru, ContactDelete
from communications.views import comm_cru, CommDelete


urlpatterns = [
    # Marketing pages
    re_path(r'^$', marketing_views.HomePage.as_view(), name="home"),

    # Subscriber related URLs
    re_path(r'^signup/$', subscr_views.subscriber_new, name='sub_new'),

    # Admin URL
    path('admin/', admin.site.urls),


    # Login/Logout URLs
    re_path(r'^login/$',
        django_views.login, {'template_name':'login.html'}, name="login"
    ),
    re_path(r'^logout/$',
        django_views.logout, {'next_page': '/login/'}
    ),


    # Account related URLs
    re_path(r'^account/new/$', account_cru, name='account_new'),
    re_path(r'^account/list/$', account_views.as_view(), name='account_list'),
    re_path(r'^account/(?P<uuid>[\w-]+)/', include('accounts.urls')),

    # Contact related URLS
    re_path(r'^contact/(?P<uuid>[\w-]+)/', include('contacts.urls')),
    re_path(r'^contact/new/$', contact_cru, name='contact_new'),
    re_path(r'^contact/(?P<pk>[\w-]+)/delete/$', ContactDelete.as_view(), name='contact_delete'),
    # Communication related URLs
    re_path(r'^comm/(?P<uuid>[\w-]+)/', include('communications.urls')),
    re_path(r'^comm/new/$', comm_cru, name='comm_new'),
    re_path(r'^comm/(?P<pk>[\w-]+)/delete/$', CommDelete.as_view(), name='comm_delete'),
]
