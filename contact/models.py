from django.db import models
from django.conf import settings # assist us to fetch user model

# Create your models here.
class Contact(models.Model):
    contact_id = models.IntegerField(primary_key=True, default=False) 
    contact_name = models.CharField(max_length=30)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=12)
    date_created = models.DateField()
    last_updated = models.DateField()
    is_archived = models.BooleanField(default=False)
    is_trashed = models.BooleanField(default=False)