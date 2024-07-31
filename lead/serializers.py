# leads/serializers.py
from rest_framework import serializers
from .models import Lead

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'source', 'created_at', 'updated_at']


