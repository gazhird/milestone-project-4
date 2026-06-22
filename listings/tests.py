from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta
from .models import Listing, Bid

User = get_user_model()


class CreateListingTest(TestCase):
    def test_create_listing(self):
        # test new listing
        user = User.objects.create_user(username="test01", password="password")
        listing = Listing.objects.create(
            make="Ford",
            model="Fiesta",
            year=2026,
            registration="TEST 001",
            mileage=100000,
            fuel="petrol",
            transmission="manual",
            condition="good",
            colour="Red",
            doors=5,
            description="Test Description 001",
            starting_price=1000,
            current_price=1000,
            ends_at=timezone.now() + timedelta(days=1),
            seller=user,
            status="active"
        )
        self.assertEqual(listing.make, "Ford")
        self.assertEqual(listing.model, "Fiesta")


class EditListingTest(TestCase):
    def test_create_listing(self):
        # test edit listing
        user = User.objects.create_user(username="test02", password="password")
        listing = Listing.objects.create(
            make="Ford",
            model="Fiesta",
            year=2026,
            registration="TEST 002",
            mileage=100000,
            fuel="petrol",
            transmission="manual",
            condition="good",
            colour="Red",
            doors=5,
            description="Test Description 002",
            starting_price=1000,
            current_price=1000, # edit current price test
            ends_at=timezone.now() + timedelta(days=1),
            seller=user,
            status="active"
        )
        # Edit price
        listing.current_price = 2000
        listing.save()
        
        updated = Listing.objects.get(id=listing.id)
        self.assertEqual(updated.current_price, 2000)


