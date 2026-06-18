from django.utils import timezone
from .models import Listing, Bid, Notification


# Find all expired auctions, change table column 'status' from 'active' to 'ended'


def check_and_close_auctions():
    
    now = timezone.now()
    
    # Get listings that have passed their end time but DB column 'status' active
    expired_listings = Listing.objects.filter(ends_at__lte=now, status="active")
    
    for listing in expired_listings:
        listing.status = "ended"
        listing.save()
        
        # Find the winning bid
        winning_bid = Bid.objects.filter(listing=listing).order_by('-bid').first()
        
        if winning_bid:
            # Set the winner and final price
            listing.winner = winning_bid.user
            listing.final_price = winning_bid.bid
            listing.save()

            # alert the Winner
            Notification.objects.create(
                user=winning_bid.user,
                listing=listing,
                message=f"Congratulations! You won the auction for the {listing.make} {listing.model} with a bid of £{winning_bid.bid:.2f}. Proceed to payment to secure it!"
            )
                    
            # alert the Seller
            Notification.objects.create(
                user=listing.seller,
                listing=listing,
                message=f"Your listing ' {listing.make} {listing.model}' has ended. It sold to {winning_bid.user.username} for £{winning_bid.bid:.2f}."
            )
        else:
            # No bids
            Notification.objects.create(
                user=listing.seller,
                listing=listing,
                message=f"Your listing ' {listing.make} {listing.model}' has ended with no bids."
            )