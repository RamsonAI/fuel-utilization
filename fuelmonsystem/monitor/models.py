from django.db import models
from django.contrib.auth.models import AbstractUser
from location_field.models.plain import PlainLocationField
import uuid

# Create your models here.

class User(AbstractUser):
    userID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role_choice = [
        ('ADMIN', 'ADMIN'),
        ('OWNER', 'OWNER'),
    ]
    role = models.CharField(choices=role_choice, max_length=10)

class Sensor(models.Model):
    sensorID = models.CharField(primary_key=True, max_length=100)
    # VIN = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='sensors', null=True)
    # serialnumber = models.ForeignKey(Generator, on_delete=models.CASCADE, related_name='sensors', null=True)

class GPStracker(models.Model):
    trackerID = models.CharField(primary_key=True, max_length=100)
    # VIN = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='gps_trackers', null=True)
    # serialnumber = models.ForeignKey(Generator, on_delete=models.CASCADE, related_name='gps_trackers', null=True)

class Vehicle(models.Model):
    VIN = models.CharField(primary_key=True, max_length=10, null=False)
    model = models.CharField(max_length=150)
    tank_capacity = models.IntegerField(default=0, null=False)
    fuel_choices = (
        ('P', 'PETROL'),
        ('D', 'DIESEL')
    )
    fuel_type = models.CharField(choices=fuel_choices, max_length=1, null=False)
    sensorID = models.ForeignKey(Sensor, on_delete=models.CASCADE,related_name='sensor_implemented')
    trackerID = models.ForeignKey(GPStracker, on_delete=models.CASCADE, related_name='tracker_implemented')
    # user = models.ForeignKey('auth.User', related_name='vehicles', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.VIN} {self.model} {self.sensorID} {self.trackerID}"

class Generator(models.Model):
    serialnumber = models.CharField(primary_key=True, max_length=100, null=False)
    tank_capacity = models.IntegerField(default=0, null=False)
    fuel_choices = (
        ('P', 'PETROL'),
        ('D', 'DIESEL')
    )
    fuel_type = models.CharField(choices=fuel_choices, max_length=1, null=False)
    sensorID = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='sensor_it_contain')
    trackerID = models.ForeignKey(GPStracker, on_delete=models.CASCADE, related_name='tracker_it_contain')

    def __str__(self):
        return f"{self.serialnumber}{self.sensorID}{self.trackerID}"

#Receives readings from the microcontroler
class SensorReading(models.Model):
    readingID = models.UUIDField(primary_key=True, default=uuid.uuid4, null=False)
    sensorID = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='readings')
    volume = models.PositiveIntegerField(blank=False)

#Receives gps location from the GPStracker
class Location(models.Model):
    locationID = models.UUIDField(primary_key=True, default=uuid.uuid4)
    trackerID = models.ForeignKey(GPStracker, on_delete=models.CASCADE, related_name='locations')
    coordinates = PlainLocationField(based_fields=['city'], zoom=7)

class SensorCallibration(models.Model):
    callibrationID = models.UUIDField(primary_key=True, default=uuid.uuid4, null=False)
    sensorID = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='callibrations')
    litres = models.PositiveBigIntegerField(null=False)
    volt = models.PositiveSmallIntegerField(null=False)

class FuelRecord(models.Model):
    recordID = models.UUIDField(primary_key=True, default=uuid.uuid4)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True, related_name='fuel_records_vehicle')
    generator = models.ForeignKey(Generator, on_delete=models.CASCADE, null=True, related_name='fuel_records_generator')
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    fuel_level = models.IntegerField()

    def get_related_object(self):
        if self.vehicle:
            return self.vehicle
        elif self.generator:
            return self.generator
        else:
            return None
