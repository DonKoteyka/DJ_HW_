from django_filters import DateFromToRangeFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsOwner
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    """ViewSet для объявлений."""
    permission_classes = (IsOwner, IsAuthenticatedOrReadOnly)
    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['creator', 'status']
    filterset_class = AdvertisementFilter

    # def perform_create(self, serializer):
    #     if Advertisement.objects.filter(status='OPEN', creator_id=self.request.user.id).count() >=10:
    #         raise ValueError('Превышение количества открытых объявлений')
    #     super().perform_create(serializer)
    # def perform_update(self, serializer):
    #     if Advertisement.objects.filter(status='OPEN', creator_id=self.request.user.id).exclude().count() >=10:
    #         raise ValueError('Превышение количества открытых объявлений')
    #     super().perform_update(serializer)

