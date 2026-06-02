from django.urls import path
from . import views


urlpatterns = [
    path("", views.list_view, name="home"),
    path("my_listings/", views.upload, name="my_listings"),
    path('vehicle/<int:listing_id>/', views.vehicle_detail, name='vehicle'),
    path('edit/', views.edit_listing, name='edit_listing'),
path('delete/<int:listing_id>/', views.delete_listing, name='delete_listing'),
    path('vehicle/<int:listing_id>/bid/', views.place_bid, name='place_bid'),
    path('notifications/', views.notifications_view, name='notifications'),
]
