from django.contrib import admin
from .models import User,Sensor,GPStracker,Vehicle,Generator,SensorCallibration,SensorReading,FuelRecord,Location

# Register your models here.

admin.site.register(User)
admin.site.register(Sensor)
admin.site.register(GPStracker)
admin.site.register(Vehicle)
admin.site.register(Generator)
admin.site.register(SensorCallibration)
admin.site.register(SensorReading)
admin.site.register(FuelRecord)
admin.site.register(Location)