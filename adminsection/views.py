from django.utils import timezone
from rest_framework.generics import GenericAPIView, ListCreateAPIView, ListAPIView
from .models import *
from .serializers import *

# Create your views here.

class ListCreateTrainDetails(ListAPIView):
    queryset = TrainDetails.objects.all()
    serializer_class = TrainDetailsSerializer

    def get_queryset(self):
        today = timezone.localdate()
        if self.request.method == 'GET':
            return TrainDetails.objects.filter(Journey_Date__gte = today)

