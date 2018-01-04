from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Subscriber(models.Model):
    user_rec = models.ForeignKey(User, on_delete=models.CASCADE,)
    address_one = models.CharField(max_length=100)
    address_two = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    stripe_id = models.CharField(max_length=30, blank=True)

    USERNAME_FIELD = "user_rec"

    class Meta:
        verbose_name_plural = 'subscribers'

    def __unicode__(self):
        return u"%s's Subscription Info" % self.user_rec
