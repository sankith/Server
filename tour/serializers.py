from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import *
from adminsection.serializers import CustomerDetailsSerializer


class ToursOfferedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToursOffered
        fields = '__all__'

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request')
        
        if request:
            if request.method != 'POST':
                fields['id'] = serializers.IntegerField(required = False)        
        return fields

class TourDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourDetails
        fields = '__all__'

    def get_fields(self):
        fields =  super().get_fields()
        request = self.context.get('request')

        if request:
            if request.method == 'GET':
                fields['customer'] = CustomerDetailsSerializer(many = True)
            if request.method == 'PUT' or request.method == 'PATCH':
                fields['id'] = serializers.IntegerField(required = False)   
        return fields
    

class DayWiseScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayWiseSchedule
        fields = "__all__"

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request')
        
        if request:
            if request.method != 'POST':
                fields['id'] = serializers.IntegerField(required = False)        
        return fields

class VisitingPlacesInTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitingPlacesInTour
        fields = "__all__"

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request')
        
        if request:
            if request.method != 'POST':
                fields['id'] = serializers.IntegerField(required = False)        
        return fields

    