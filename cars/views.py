from django.shortcuts import render
from cars.models import CarMaker , Cars
from .serializers import CarMakerSerializer, CarsSerializer
from rest_framework import viewsets
from url_filter.integrations.drf import DjangoFilterBackend

class CarsViewSet(viewsets.ModelViewSet):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['car_model_name', 'car_make_year', 'car_maker_name']
class CarMakerViewSet(viewsets.ModelViewSet):
    queryset = CarMaker.objects.all()
    serializer_class = CarMakerSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['name']
 