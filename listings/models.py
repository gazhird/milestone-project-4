from django.db import models
from django.conf import settings
from django.utils import timezone
from cloudinary.models import CloudinaryField

# Database models / listings

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
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="listings")
    highest_bidder = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, related_name="highest_bids")
    winner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, related_name="won_listings")
    final_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        ordering = ["-created_at"]

    @property
    def is_expired(self):
        #  return true if expired
        return timezone.now() > self.ends_at

    def __str__(self):
        return f"{self.make or 'No Make'} {self.model or 'No Model'}"
    

class Bid(models.Model):
    # Connects a foreign key to the listing class above
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bids')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='placed_bids')
    bid = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-bid']

    def __str__(self):
        return f"£{self.bid} on {self.listing.make} by {self.user.username if self.user else 'Unknown'}"


class Notification(models.Model):
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Alert for {self.user.username if self.user else 'Unknown'}: {self.message[:30]}"