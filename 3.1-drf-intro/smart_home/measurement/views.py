# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Measurment, Sensor
from .serializers import SensorDetailSerializer


# @api_view(['GET', 'POST'])
# def api(request):
#     get_bd = Sensor.objects.all()
#     data = SensorSerializer(get_bd, many=True)
#     return Response(data.data)
#
# class API(APIView):
#     def get(self, request):
#         get_bd = Sensor.objects.all()
#         data = SensorDetailSerializer(get_bd, many=True)
#         return Response(data.data)
#
#     def post(self, request):
#         res = request.GET
#         new_sensor = Sensor(
#             name=res.get('name'),
#             description=res.get('description')
#         )
#         new_sensor.save()
#         return Response('новая запись добавлена')
class API(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def post(self, request):
        res = request.GET
        new_sensor = Sensor(
            name=res.get('name'),
            description=res.get('description')
        )
        new_sensor.save()
        return Response('новая запись добавлена')

    def patch(self, request):
        res = request.GET


        pass
