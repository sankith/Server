from django.urls import path
from . import views

urlpatterns = [
    path('traindetails/', views.ListCreateTrainDetails.as_view())
]