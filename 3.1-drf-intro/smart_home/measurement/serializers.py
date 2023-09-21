from rest_framework import serializers

from .models import Sensor, Measurment


# class SensorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Sensor
#         fields = ['id','name', 'description']
    # name = serializers.CharField()
    # description = serializers.CharField()

class MeasurementSerializer(serializers.ModelSerializer):
    sensor = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Measurment
        fields = ['id','temperature', 'created_at', 'sensor']


class SensorDetailSerializer(serializers.ModelSerializer):
    # measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']
