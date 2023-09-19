from django.contrib import admin

from .models import Sensor, Measurment


# Register your models here.

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
@admin.register(Measurment)
class MeasurmentsAdmin(admin.ModelAdmin):
    list_display = ['temperature', 'created_at', 'sensor']
