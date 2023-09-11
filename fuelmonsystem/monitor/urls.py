from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from monitor import views

urlpatterns = [
    path('monitor/users', views.UserList.as_view()),
    path('monitor/sensors', views.SensorList.as_view()),
    path('monitor/trackers', views.GPStrackerList.as_view()),
    path('monitor/vehicles', views.VehicleList.as_view()),
    path('monitor/generators', views.GeneratorList.as_view()),
    path('monitor/fuelrecords', views.FuelRecordList.as_view()),
    path('monitor/locations', views.LocationList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

