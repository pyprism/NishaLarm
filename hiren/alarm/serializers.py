from rest_framework import serializers
from .models import Api, Nisha


class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Api


class NishaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nisha