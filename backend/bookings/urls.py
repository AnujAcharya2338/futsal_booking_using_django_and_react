from django.urls import path
from . import views

urlpatterns = [
    path('api/courts/',views.get_courts),
    path('api/timeslot/',views.get_timeslot),
    path('api/booking/',views.get_booking),

]