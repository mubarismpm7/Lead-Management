from rest_framework import serializers
from leadApp.models import Lead

class LeadSerializer(serializers.ModelSerializer):
    #source=serializers.ChoiceField(choices=Lead.SOURCE_CHOICES)
    class Meta:
        model=Lead
        fields="__all__"
        read_only_fields=['id',"added_date"]