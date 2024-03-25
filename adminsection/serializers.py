from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import CustomerDetails, TrainDetails

class TrainDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainDetails
        fields = "__all__"

class CustomerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDetails
        fields = "__all__"