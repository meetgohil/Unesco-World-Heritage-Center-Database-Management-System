#models.py
from django.db import models


class InstModel(models.Model):
    institute_id = models.IntegerField(primary_key=True)
    institute_name=models.CharField(max_length=500)
    officer=models.CharField(max_length=100)
    address=models.CharField(max_length=1000)
    contact=models.CharField(max_length=20)
    class Meta:
        db_table="local_institute_agency"

class SiteModel(models.Model):
    s_id=models.IntegerField(primary_key=True)
    site_name=models.CharField(max_length=1000)
    address=models.CharField(max_length=1000)
    latitude=models.FloatField()
    longitude=models.FloatField()
    area=models.FloatField()
    country_code=models.IntegerField()
    category=models.CharField(max_length=50)
    buffer_zone=models.FloatField()
    historical_detail=models.CharField(max_length=5000)
    ownership=models.CharField(max_length=1000)
    institute_id=models.IntegerField()
    class Meta:
        db_table="site_detail"

class CountryModel(models.Model):
    country_code=models.IntegerField(primary_key=True)
    country_name=models.CharField(max_length=100)
    donor_id=models.IntegerField()
    region=models.CharField(max_length=100)
    veto_power=models.BooleanField()
    representative=models.CharField(max_length=100)
    class Meta:
        db_table="member_country"