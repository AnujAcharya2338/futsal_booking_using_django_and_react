from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *


@api_view(['GET'])

def get_courts(request):
    courts = Court.objects.all()
    court_serializer = CourtSerializers(courts, many = True)
    return Response (court_serializer.data)

@api_view(['GET'])

def get_timeslot(request):
    timeslot = Timeslot.objects.all()
    time_serializers = TimeslotSerializers(timeslot, many =True)
    return Response (time_serializers.data)

@api_view(['GET'])

def get_booking(request):
    booking = Booking.objects.all()
    booking_serializers = BookingSerializers(booking, many = True)
    return Response (booking_serializers.data)

# Create your views here.
