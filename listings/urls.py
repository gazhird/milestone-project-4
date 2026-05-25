from django.urls import path
from . import views


urlpatterns = [
    path("my_listings/", views.upload, name="my_listings"),
    path("", views.list_view, name="home"),
    path('vehicle/<int:listing_id>/', views.vehicle_detail, name='vehicle'),
    path('edit/', views.edit_listing, name='edit_listing'),
    path('delete/<int:listing_id>/', views.delete_listing, name='delete_listing'),
]
