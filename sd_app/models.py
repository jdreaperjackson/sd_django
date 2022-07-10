from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime


class Transaction(models.Model):
    """
    Transaction model
    """        
    # Amount being purchased
    gallons_requested = models.FloatField()
    # Location where transaction occurred, true if in state, false if out of state.
    location = models.CharField(max_length=100)    
    # Date and time of desired delivery
    delivery_date = models.CharField(max_length=15)
    # User who made the transaction
    suggested_price = models.CharField(max_length=5, default='$4.57')
    total_amount_due = models.CharField(max_length=6, default='$1,234')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Gallons requested: " + str(self.gallons_requested) + " gal. Location: " + str(self.location) + ". Delivery Date: " + str(self.delivery_date) + ". Suggested price: " + str(self.suggested_price) + ". Total amount due: " + str(self.total_amount_due)

STATE_CHOICES = (
    ('al','AL'),
    ('ak','AK'),
    ('az','AZ'),
    ('ar','AR'),
    ('ca','CA'),
    ('co','CO'),
    ('ct','CT'),
    ('de','DE'),
    ('fl','FL'),
    ('ga','GA'),
    ('hi','HI'),
    ('id','ID'),
    ('il','IL'),
    ('in','IN'),
    ('ia','IA'),
    ('ks','KS'),
    ('ky','KY'),
    ('la','LA'),
    ('me','ME'),
    ('md','MD'),
    ('ma','MA'),
    ('mi','MI'),
    ('mn','MN'),
    ('ms','MS'),
    ('mo','MO'),
    ('mt','MT'),
    ('ne','NE'),
    ('nv','NV'),
    ('nh','NH'),
    ('nj','NJ'),
    ('nm','NM'),
    ('ny','NY'),
    ('nc','NC'),
    ('nd','ND'),
    ('oh','OH'),
    ('ok','OK'),
    ('or','OR'),
    ('pa','PA'),
    ('ri','RI'),
    ('sc','SC'),
    ('sd','SD'),
    ('tn','TN'),
    ('tx','TX'),
    ('ut','UT'),
    ('vt','VT'),
    ('va','VA'),
    ('wa','WA'),
    ('wv','WV'),
    ('wi','WI'),
    ('wy','WY'),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    zipcode = models.CharField(max_length=5)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()