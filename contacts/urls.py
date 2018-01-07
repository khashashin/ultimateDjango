from django.urls import re_path
from .views import contact_detail, contact_cru

urlpatterns = [
    re_path(r'^$', contact_detail, name="contact_detail"),
    re_path(r'^edit/$', contact_cru, name='contact_update'),

]
