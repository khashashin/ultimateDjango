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
from django.urls import path, re_path
from marketing.views import HomePage
from subscribers import views

urlpatterns = [
    # Marketing pages
    re_path(r'^$', HomePage.as_view(), name="home"),

    # Subscriber related URLs
    re_path(r'^signup/$', views.subscriber_new, name='sub_new'),

    # Admin URL
    path('admin/', admin.site.urls),


    # Login/Logout URLs
    re_path(r'^login/$',
    'django.contrib.auth.views.login', {'template_name': 'login.html'}
    ),
    re_path(r'^logout/$',
        'django.contrib.auth.views.logout', {'next_page': '/login/'}
    ),


    # Account related URLs


    # Contact related URLS


    # Communication related URLs
]
