# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, ListCreateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Measurment, Sensor
from .serializers import SensorDetailSerializer, MeasurementSerializer


# class API(APIView):
class API(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

    # def get(self, request):
    #     get_bd = Sensor.objects.all()
    #     data = SensorDetailSerializer(get_bd, many=True)
    #     return Response(data.data)
    #
    # def post(self, request):
    #     res = request.GET
    #     new_sensor = Sensor(
    #         name=res.get('name'),
    #         description=res.get('description')
    #     )
    #     new_sensor.save()
    #     return Response('новая запись добавлена')


class APIputch(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    # def get(self, request, pk):
    #     sensor_get = Sensor.objects.get(id=pk)
    #     data = SensorDetailSerializer(sensor_get)
    #     return Response(data.data)
    #
    # def patch(self, request, pk):
    #     res = request.GET
    #     sensor_update = Sensor.objects.get(id=pk)
    #     sensor_update.description = res.get('description')
    #     sensor_update.save()
    #     return Response('запись обновлена')


class APIMesurments(CreateAPIView):
    get_queryset = Measurment.objects.all()
    serializer_class = MeasurementSerializer


    # def post(self, request, *args, **kwargs):
    #     sensor = request.data['sensor']
    #     temperature = request.data['temperature']
    #     file = request.data['image']
    #     user = Measurment.objects.get(sensor=sensor)
    #     user.image = file
    #     user.sensor = sensor
    #     user.temperature = temperature
    #     user.save()
    #     return Response("Image updated!", status=status.HTTP_200_OK)
