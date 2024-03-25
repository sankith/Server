from django.db import models

# Create your models here.
class ToursOffered(models.Model):
    Tour_Name = models.CharField(max_length=50)
    Description = models.TextField()

    def __str__(self):
        return self.Tour_Name + self.Description

    class Meta:
        db_table = 'SLT_TOURS_OFFERED'



class TourDetails(models.Model):
    Tour = models.ForeignKey(ToursOffered, on_delete=models.CASCADE)
    Package_Cost = models.IntegerField()
    Start_Date = models.DateField( auto_now=False, auto_now_add=False)
    End_Date = models.DateField(auto_now=False, auto_now_add=False)
    No_Of_Days = models.IntegerField()
    customer = models.ManyToManyField('adminsection.CustomerDetails')

    class Meta:
        db_table = 'SLT_TOUR_DETAILS'

class DayWiseSchedule(models.Model):
    Tour = models.ForeignKey(ToursOffered, on_delete=models.CASCADE)
    Day = models.IntegerField()
    Schedule = models.TextField()

    class Meta:
        db_table = "SLT_DAY_WISE_SCHEDULE"


class VisitingPlacesInTour(models.Model):
    Tour = models.ForeignKey(ToursOffered,  on_delete=models.CASCADE)
    Place = models.CharField(max_length = 255)

    class Meta:
        db_table = "SLT_VISTING_PLACE_IN_TOUR"


