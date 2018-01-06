from django.urls import re_path
from .views import contact_detail

urlpatterns = [
    re_path(r'^$', contact_detail, name="contact_detail"),
]
