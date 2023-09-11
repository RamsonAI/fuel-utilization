from django.shortcuts import render
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from monitor.models import User, Vehicle, Generator, Sensor, SensorReading, Location, FuelRecord,GPStracker
from monitor.serializer import UserSerializer,FuelRecordSerializer, VehicleSerializer, GeneratorSerializer, SensorSerializer, GPStrackerSerializer, LocationSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class UserList(APIView):
    """
    get users list
    """
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
class VehicleList(APIView):
    """
    list all vehicle or register a vehicle
    """
    def get(self, request, format=None):
        vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = VehicleSerializer(data=request.data)
        if serializer .is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )
    
class GeneratorList(APIView):
    """
    list all generators or register a generator
    """
    def get(self, request, format=None): 
        generators = Generator.objects.all()
        serializer = GeneratorSerializer(generators, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = GeneratorSerializer(data=request.data)
        if serializer .is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )
    
class SensorList(APIView):
    """
    list all sensors or register sensor
    """
    def get(self, request, format=None):
        sensors = Sensor.objects.all()
        serializer = SensorSerializer(sensors, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = SensorSerializer(data=request.data)
        if serializer .is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LocationList(APIView):
    """
    list tracked locations 
    """
    def get(self, request, format=None):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)
    
    # def post
    
class GPStrackerList(APIView):
    """
    list all GPStracker or register GPStracker
    """
    def get(self, request, format=None):
        trackers = GPStracker.objects.all()
        serializer = GPStrackerSerializer(trackers, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = GPStrackerSerializer(data=request.data)
        if serializer .is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FuelRecordList(APIView):
    """
    get fuel record list 
    """
    def get(self, request, format=None):
        fuelrecords = FuelRecord.objects.all()
        serializer = FuelRecordSerializer(fuelrecords, many=True)
        return Response(serializer.data)

