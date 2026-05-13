from django.urls import path
from . import views


urlpatterns = [
    path("my_listings/", views.upload, name="my_listings"),
    path("", views.list_view, name="home"),
    path('vehicle/<int:listing_id>/', views.vehicle_detail, name='vehicle'),
]