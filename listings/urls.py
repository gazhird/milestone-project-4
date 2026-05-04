from django.urls import path
from . import views

app_name = "listings"

urlpatterns = [
    path("upload/", views.upload, name="upload"),
    path("", views.list_view, name="stock"),
]