# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Measurment, Sensor
from .serializers import SensorDetailSerializer


# class API(APIView):
class API(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


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


class APIMesurments(APIView):
    # def post(self, request):
    #     res = request.GET
    #     new_measurmet = Sensor(
    #         sensor=res.get('sensor'),
    #         temperature=res.get('temperature')
    #     )
    #     new_measurmet.save()
    #     return Response('новая запись добавлена')
    pass
