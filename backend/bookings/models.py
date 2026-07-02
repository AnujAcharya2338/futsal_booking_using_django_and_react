from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Court(models.Model):
    court_name = models.CharField(max_length=30)
    court_description = models.CharField(max_length=200)
    price_per_hour = models.IntegerField()
    location = models.CharField(max_length=100)
    def __str__(self):
        return self.court_name

class Timeslot(models.Model):
    courts = models.ForeignKey(Court, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_booked = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.courts} | {self.start_time} - {self.end_time}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    courts = models.ForeignKey(Court, on_delete=models.CASCADE)
    timeslot = models.ForeignKey(Timeslot, on_delete=models.CASCADE)
    payment_status = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.user} - {self.courts} - {self.timeslot}"
    

