from django.urls import path
from .views import ListCreateTourOffered

from . import views

urlpatterns = [
    path("", views.ListCreateTourOffered.as_view()),
    path("tour/delete/<int:pk>", views.ListCreateTourOffered.as_view()),
    path("tourdetails/delete/<int:pk>", views.TourDetails.as_view()),
    path("tourdetails/", views.TourDetails.as_view()),
    path("daywise/", views.DayWiseScheduleApi.as_view()),
    path("daywise/tour/<int:Tour>", views.DayWiseScheduleApi.as_view()),
    path("visitingplaces/delete/<int:pk>", views.VisitingPlacesApi.as_view()),
    path("visitingplaces/", views.VisitingPlacesApi.as_view()),
    path("visitingplaces/tour/<int:Tour>", views.VisitingPlacesApi.as_view()),




]