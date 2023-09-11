from monitor.models import User, Vehicle, Generator, Sensor, SensorReading, Location, FuelRecord, GPStracker
from rest_framework import serializers

# from rest_framework.

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['userID', 'role']

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['VIN', 'model', 'tank_capacity', 'fuel_type', 'sensorID', 'trackerID']

class GeneratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Generator
        fields = ['serialnumber', 'tank_capacity', 'fuel_type', 'sensorID', 'trackerID']

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['sensorID']

class GPStrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPStracker
        fields = ['trackerID']

class FuelRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelRecord
        fields = ['recordID', 'vehicle', 'generator', 'date', 'time', 'fuel_level']

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['locationID', 'trackerID', 'coordinates']