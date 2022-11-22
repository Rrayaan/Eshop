from rest_framework import serializers
from .models import signup


class eshopserializer(serializers.ModelSerializer):
    class Meta:
        model = signup
        fields = '__all__'
