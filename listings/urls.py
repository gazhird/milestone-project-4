from django.urls import path
from . import views


urlpatterns = [
    path("upload/", views.upload, name="upload"),
    path("", views.list_view, name="home"),
    path('vehicle/<int:listing_id>/', views.vehicle_detail, name='vehicle'),
]