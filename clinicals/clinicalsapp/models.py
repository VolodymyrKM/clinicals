from django.db import models


# Create your models here.

class Patient(models.Model):
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class ClinicalData(models.Model):
    COMPONENT_NAMES = [('hw', 'Height/Weight'), ('bp', 'Blood Pressure'), ('heartrate', 'Heart Rate')]
    component_name = models.CharField(max_length=20, choices=COMPONENT_NAMES)
    component_value = models.CharField(max_length=20)
    measure_date_time = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)


