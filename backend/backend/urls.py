from django.contrib import admin
from django.urls import include, path
from backend import views  # replace 'your_app' with your actual app name
from bookings import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bookings.urls'))
]