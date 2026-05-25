from django.db import models
from django.conf import settings
from django.utils import timezone
from cloudinary.models import CloudinaryField


class Listing(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    registration = models.CharField(max_length=20)
    mileage = models.PositiveIntegerField()

    # Select options
    FUEL_CHOICES = [
        ("petrol", "Petrol"),("diesel", "Diesel"),("electric", "Electric"),("hybrid", "Hybrid"),
    ]
    fuel = models.CharField(max_length=20, choices=FUEL_CHOICES)

    TRANSMISSION_CHOICES = [
        ("manual", "Manual"),("automatic", "Automatic"),
    ]
    transmission = models.CharField(max_length=20, choices=TRANSMISSION_CHOICES)

    CONDITION_CHOICES = [
        ("excellent", "Excellent"),("good", "Good"),("average", "Average"),("nonrunner", "Non Runner"),
    ]
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES)

    colour = models.CharField(max_length=30)
    doors = models.PositiveIntegerField()
    description = models.TextField()


    starting_price = models.DecimalField(max_digits=10, decimal_places=2)
    reserve_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    current_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

 
    image1 = CloudinaryField('image', folder='top_bidder/vehicles/', blank=True, null=True)
    image2 = CloudinaryField('image', folder='top_bidder/vehicles/', blank=True, null=True)
    image3 = CloudinaryField('image', folder='top_bidder/vehicles/', blank=True, null=True)
    image4 = CloudinaryField('image', folder='top_bidder/vehicles/', blank=True, null=True)


    created_at = models.DateTimeField(auto_now_add=True)
    ends_at = models.DateTimeField()
    status = models.CharField(max_length=20, default="active")


    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="listings"
    )
    highest_bidder = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, related_name="highest_bids"
    )
    winner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, related_name="won_listings"
    )
    final_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        ordering = ["-created_at"]

    @property
    def is_expired(self):
        #  return true if expired
        return timezone.now() > self.ends_at

    def __str__(self):
        return f"{self.make or 'No Make'} {self.model or 'No Model'}"