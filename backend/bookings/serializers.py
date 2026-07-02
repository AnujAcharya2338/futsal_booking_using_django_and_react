from rest_framework import serializers
from .models import *

class CourtSerializers(serializers.ModelSerializer):
    class Meta:
        model = Court
        fields = '__all__'

class TimeslotSerializers(serializers.ModelSerializer):
    class Meta:
        model = Timeslot
        fields = '__all__'
        

class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
