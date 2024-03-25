from django.http import Http404
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListCreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, RetrieveAPIView
from .models import *
from .serializers import *
from rest_framework import exceptions
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response

# Create your views here.
class ListCreateTourOffered(ListCreateAPIView, UpdateAPIView, DestroyAPIView):
    queryset = ToursOffered.objects.all()
    serializer_class = ToursOfferedSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')
        if not pk:
            pk = self.request.data.get('id')
        
        if not pk:
            raise exceptions.ValidationError("Primary key must be provided")
   
        queryset = self.get_queryset()
        try:
            return queryset.get(pk=pk)
        except queryset.model.DoesNotExist:
            raise Http404

    def perform_create(self, serializer):
        query_set = ToursOffered.objects.filter(Tour_Name = self.request.data.get('Tour_Name'))
        if query_set.exists():
            raise ValidationError('Tour Already Exist')
        return super().perform_create(serializer)
    

class TourDetails(ListCreateAPIView, UpdateAPIView, DestroyAPIView ):
    queryset = TourDetails.objects.all()
    serializer_class = TourDetailsSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')
        if not pk:
            pk = self.request.data.get('id')
        
        if not pk:
            raise exceptions.ValidationError("Primary key must be provided")
   
        queryset = self.get_queryset()
        try:
            return queryset.get(pk=pk)
        except queryset.model.DoesNotExist:
            raise Http404

class DayWiseScheduleApi(ListCreateAPIView, UpdateAPIView):
    queryset = DayWiseSchedule.objects.all()
    serializer_class = DayWiseScheduleSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')
        if not pk:
            pk = self.request.data.get('id')
        
        if not pk:
            raise exceptions.ValidationError("Primary key must be provided")
   
        queryset = self.get_queryset()
        try:
            return queryset.get(pk=pk)
        except queryset.model.DoesNotExist:
            raise Http404

    def list(self, request, *args, **kwargs):
        query_set = DayWiseSchedule.objects.filter(Tour = self.kwargs.get('Tour'))
        serializer = DayWiseScheduleSerializer(query_set, many = True)
        return Response(serializer.data)
    

class VisitingPlacesApi(ListCreateAPIView, UpdateAPIView, DestroyAPIView):
    queryset = VisitingPlacesInTour.objects.all()
    serializer_class = VisitingPlacesInTourSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')
        if not pk:
            pk = self.request.data.get('id')
        
        if not pk:
            raise exceptions.ValidationError("Primary key must be provided")
   
        queryset = self.get_queryset()
        try:
            return queryset.get(pk=pk)
        except queryset.model.DoesNotExist:
            raise Http404

    # def list(self, request, *args, **kwargs):
    #     query_set = VisitingPlacesInTour.objects.filter(Tour = self.kwargs.get('Tour'))
    #     serializer = VisitingPlacesInTourSerializer(query_set, many = True)
    #     return Response(serializer.data)

