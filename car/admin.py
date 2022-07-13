from django.contrib import admin
from car.models import Car, CarType, CarMissionType, CarManagerMission, CarManager

admin.site.register(Car)
admin.site.register(CarType)
admin.site.register(CarMissionType)
admin.site.register(CarManagerMission)
admin.site.register(CarManager)
