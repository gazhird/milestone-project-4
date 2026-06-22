from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta
from .models import Listing

User = get_user_model()

# CRUD tests 

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
    def test_edit_listing(self):
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
            current_price=1000, # update current price 
            ends_at=timezone.now() + timedelta(days=1),
            seller=user,
            status="active"
        )
        # Edit price
        listing.current_price = 2000
        listing.save()
        
        updated = Listing.objects.get(id=listing.id)
        self.assertEqual(updated.current_price, 2000)


class DelListingTest(TestCase):
    def test_del_listing(self):
        # test delete listing
        user = User.objects.create_user(username="test03", password="password")
        listing = Listing.objects.create(
            make="Ford",
            model="Fiesta",
            year=2026,
            registration="TEST 003",
            mileage=100000,
            fuel="petrol",
            transmission="manual",
            condition="good",
            colour="Red",
            doors=5,
            description="Test Description 003",
            starting_price=1000,
            current_price=1000, 
            ends_at=timezone.now() + timedelta(days=1),
            seller=user,
            status="active"
        )
        listing_id = listing.id
        listing.delete()
        with self.assertRaises(Listing.DoesNotExist):
            Listing.objects.get(id=listing_id)
