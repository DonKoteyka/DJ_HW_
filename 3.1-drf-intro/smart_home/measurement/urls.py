from django.urls import path

from measurement.views import API, APIputch, APIMesurments

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', API.as_view()),
    path('sensors/<pk>/', APIputch.as_view()),
    path('measurements/', APIMesurments.as_view()),
]
