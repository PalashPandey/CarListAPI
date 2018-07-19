from rest_framework import serializers
from .models import CarMaker, Cars


class CarMakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMaker  
        fields = '__all__'


class CarsSerializer(serializers.ModelSerializer):
    car_maker_name = CarMakerSerializer()
    
    class Meta: 
        model = Cars
        fields = '__all__'