from rest_framework import serializers
from .models import BogPost

class BogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BogPost
        fields = '__all__'