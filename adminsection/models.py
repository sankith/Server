from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator

# Create your models here.
class TrainDetails(models.Model):
    Train_No = models.IntegerField()
    Journey_Date = models.DateField(auto_now=False, auto_now_add=False)
    Tour = models.ForeignKey("tour.ToursOffered", on_delete=models.CASCADE)

    class Meta:
        db_table = 'SLT_TOURS_TRAIN_DETAILS'

class CustomerDetails(models.Model):
    Name = models.CharField(max_length=255)
    Gender = models.CharField(max_length=50)
    Phone_No = PhoneNumberField(region='IN')
    Address = models.CharField(max_length=500)
    Aadhaar_No = models.BigIntegerField(validators=[
            RegexValidator(
                r'^\d{12}$',
                'Aadhaar number must be exactly  12 digits',
                'Invalid number'
            )
        ])
    Dob = models.DateField()

    class Meta:
        db_table = 'SLT_CUSTOMER_DETAILS'