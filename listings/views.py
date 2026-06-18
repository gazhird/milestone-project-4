from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
from django.utils import timezone
from .models import Listing, Bid, Notification
from .utils import check_and_close_auctions


@login_required
def upload(request):

    # handles the upload form my_listings.html 

    if request.method == "POST":
    
        make = request.POST.get("make")
        model = request.POST.get("model")
        year = request.POST.get("year")
        registration = request.POST.get("registration")
        mileage = request.POST.get("mileage")
        fuel = request.POST.get("fuel")
        transmission = request.POST.get("transmission")
        condition = request.POST.get("condition")
        colour = request.POST.get("colour")
        doors = request.POST.get("doors")
        description = request.POST.get("description")
        starting_price = request.POST.get("starting_price")
        reserve_price = request.POST.get("reserve_price")
        end_date = request.POST.get("end_date")
        end_time = request.POST.get("end_time")


        ends_at_str = f"{end_date} {end_time}"
        ends_at = datetime.strptime(ends_at_str, "%Y-%m-%d %H:%M")
        ends_at = timezone.make_aware(ends_at)

        image1 = request.FILES.get("image1")
        image2 = request.FILES.get("image2")
        image3 = request.FILES.get("image3")
        image4 = request.FILES.get("image4")

        listing = Listing(
            make=make,
            model=model,
            year=year,
            registration=registration,
            mileage=mileage,
            fuel=fuel,
            transmission=transmission,
            condition=condition,
            colour=colour,
            doors=doors,
            description=description,
            starting_price=starting_price,
            reserve_price=reserve_price,
            current_price=starting_price,
            image1=image1,
            image2=image2,
            image3=image3,
            image4=image4,
            ends_at=ends_at,
            seller=request.user,
            status="active"
        )
        listing.save()

        return redirect("home")

    user_listings = Listing.objects.filter(seller=request.user)
    return render(request, "my_listings.html", {"listings": user_listings})


# fetches vehicle data and shows as basic list on index.html 
def list_view(request):
    listings = Listing.objects.all()
    return render(request, "index.html", {"listings": listings})


# show tailored listings on index.html (add extra later)
def home(request):
    listings = Listing.objects.all()
    return render(request, "index.html", {"listings": listings})

# shows a single selected vehicles details, checks if expired. vehicle.html
def vehicle_detail(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)

    # update status column from active to ended
    if listing.is_expired and listing.status == "active":
        listing.status = "ended"
        listing.save(update_fields=['status'])

    context = {
        'listing': listing,
        'is_expired': listing.is_expired, 
    }

    return render(request, 'vehicle.html', {'listing': listing})


# Handles the edit form my_listings.html
@login_required
def edit_listing(request):
    
    if request.method == "POST":

        # id from edit form
        listing_id = request.POST.get("edit_id")
        # fetch records
        listing = get_object_or_404(Listing, id=listing_id)

        listing.make = request.POST.get("edit_make")
        listing.model = request.POST.get("edit_model")
        listing.year = request.POST.get("edit_year")
        listing.registration = request.POST.get("edit_registration")
        listing.mileage = request.POST.get("edit_mileage")
        listing.fuel = request.POST.get("edit_fuel")
        listing.transmission = request.POST.get("edit_transmission")
        listing.condition = request.POST.get("edit_condition")
        listing.colour = request.POST.get("edit_colour")
        listing.doors = request.POST.get("edit_doors")
        listing.description = request.POST.get("edit_description")
        listing.starting_price = request.POST.get("edit_start_price")
    

        end_date = request.POST.get("edit_end_date")
        end_time = request.POST.get("edit_end_time")
        if end_date and end_time:
            ends_at_str = f"{end_date} {end_time}"
            ends_at = datetime.strptime(ends_at_str, "%Y-%m-%d %H:%M")
            listing.ends_at = timezone.make_aware(ends_at)

        if request.FILES.get("edit_image1"):
            listing.image1 = request.FILES.get("edit_image1")
        if request.FILES.get("edit_image2"):
            listing.image2 = request.FILES.get("edit_image2")
        if request.FILES.get("edit_image3"):
            listing.image3 = request.FILES.get("edit_image3")
        if request.FILES.get("edit_image4"):
            listing.image4 = request.FILES.get("edit_image4")

        listing.save()
        return redirect('my_listings')

# delete listing if seller. my_listings.html
@login_required
def delete_listing(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    
    if listing.seller == request.user:
        listing.delete()
        
    return redirect('my_listings')


# checks if new bid is higher, notify the out-bidden user
@login_required
def place_bid(request, listing_id):
    if request.method == "POST":
        bid_amount_raw = request.POST.get('bid_amount')

        # stop empty values
        if not bid_amount_raw or bid_amount_raw.strip() == "":
            messages.error(request, "Invalid bid amount.")
            return redirect('vehicle', listing_id=listing_id)
            
        # stop invalid / bad formatting/characters
        try:
            bid_amount = float(bid_amount_raw)
        except (TypeError, ValueError):
            messages.error(request, "Invalid bid amount format entered.")
            return redirect('vehicle', listing_id=listing_id)

        listing = get_object_or_404(Listing, id=listing_id)
        
        # block bids on expired items
        if listing.is_expired:
            if listing.status == "active":
                listing.status = "ended"
                listing.save(update_fields=['status'])
                
            messages.error(request, "This auction has already ended!")
            return redirect('vehicle', listing_id=listing.id)

        # save bid if it's higher than current price
        if bid_amount > float(listing.current_price):
            
            # find previous highest bidder, before updating the price
            previous_highest_bid = Bid.objects.filter(listing=listing).order_by('-bid').first()
            
            # Create the new Bid record
            Bid.objects.create(
                user=request.user,
                listing=listing,
                bid=bid_amount
            )
            
            # update the listing to show the new highest price
            listing.current_price = bid_amount
            listing.save()

            # notify previous bidder if someone outbids them
            if previous_highest_bid and previous_highest_bid.user != request.user:
                Notification.objects.create(
                    user=previous_highest_bid.user,
                    listing=listing,
                    message=f"You have been outbid on the {listing.make} {listing.model}! The new highest bid is £{bid_amount:.2f}."
                )
            
            # notify seller when a new bid is placed
            if listing.seller != request.user: 
                Notification.objects.create(
                    user=listing.seller,
                    listing=listing,
                    message=f"New bid placed! Someone offered £{bid_amount:.2f} on your listing: {listing.make} {listing.model}."
                )
            
            messages.success(request, f"Success! Your bid of £{bid_amount:.2f} has been placed.")
        else:
            messages.error(request, "Your bid must be higher than the current price.")
            
        return redirect('vehicle', listing_id=listing.id)

    return redirect('vehicle', listing_id=listing_id)


@login_required
def notifications_view(request):
    check_and_close_auctions()
    
    # Get notifications for the current user
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    notifications_list = list(notifications)
    notifications.filter(is_read=False).update(is_read=True)
    return render(request, 'notifications.html', {
        'notifications': notifications_list
    })


# stripe payments 

import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def delete_notification(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id, user=request.user)
    notification.delete()
    return redirect('notifications')


@login_required
def create_checkout_session(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    
    if listing.winner != request.user:
        messages.error(request, "You are not the winner of this auction.")
        return redirect('notifications')
    
    if listing.status != "ended":
        messages.error(request, "This auction has not ended yet.")
        return redirect('notifications')
    
    if listing.paid:
        messages.info(request, "You have already paid for this item.")
        return redirect('notifications')
    
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'gbp',
                    'product_data': {
                        'name': f"{listing.make} {listing.model}",
                    },
                    'unit_amount': int(listing.current_price * 100),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri('/payment/success/'),
            cancel_url=request.build_absolute_uri('/payment/cancel/'),
        )
        return redirect(session.url, code=303)
        
    except Exception as e:
        messages.error(request, f"Payment failed: {str(e)}")
        return redirect('notifications')


def payment_success(request):
    messages.success(request, "Payment successful! Thank you for your purchase.")
    return redirect('notifications')

def payment_cancel(request):
    messages.error(request, "Payment was cancelled.")
    return redirect('notifications')