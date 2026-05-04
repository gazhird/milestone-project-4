from django.contrib import admin
from .models import Listing

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ["make", "model", "year", "starting_price", "ends_at", "status", "seller"]
    list_filter = ["status", "fuel", "transmission"]
    search_fields = ["make", "model", "registration"]