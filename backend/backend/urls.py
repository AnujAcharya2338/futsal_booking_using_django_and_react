from django.contrib import admin
from django.urls import path
from backend import views  # replace 'your_app' with your actual app name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/hello/', views.hello),
    path('', views.hello),
]