from django.urls import re_path
from .views import comm_detail


urlpatterns = [
    re_path(r'^$', comm_detail, name="comm_detail"),
]
