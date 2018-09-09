from django.db import models
from schools.models import School

class Schooldata(models.Model):
    # id = models.AutoField(primary_key=True)
    # school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    # year = models.IntegerField()
    # week = models.IntegerField()
    # month = models.IntegerField()
    # elect_eur = models.FloatField()
    # elect_kwh = models.FloatField()
    # heating_eur = models.FloatField()
    # heating_kwh = models.FloatField()
    # water_eur = models.FloatField()
    # water_litres = models.FloatField()

    # def __str__(self):
    #     return self.school_id
    title = models.TextField()