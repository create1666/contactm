from .models import Contact
from rest_framework import serializers


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['contact_id','contact_name', 'is_trashed', 'user', 'is_archived', 'date_created', "last_updated"]
