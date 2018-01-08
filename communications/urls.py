from django.urls import re_path
from .views import comm_detail, comm_cru


urlpatterns = [
    re_path(r'^$', comm_detail, name="comm_detail"),
    re_path(r'^edit/$', comm_cru, name='comm_update'),
]
