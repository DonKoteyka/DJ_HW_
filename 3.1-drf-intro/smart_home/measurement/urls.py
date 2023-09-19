from django.urls import path

from measurement.views import  API

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors', API.as_view()),
]
