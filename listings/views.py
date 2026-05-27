from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.utils import timezone
from .models import Listing


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
    return render(request, "listings/index.html", {"listings": listings})


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
# @login_required
# def place_bid(request, listing_id):
#     if request.method == "POST":
#         listing = get_object_or_404(Listing, id=listing_id)
        
#         # check item not expired before bid submitted
#         if listing.is_expired:
#             if listing.status == "active":
#                 listing.status = "ended"
#                 listing.save(update_fields=['status'])
                
#             # stop the user from bidding
#             messages.error(request, "This auction has already ended!")
#             return redirect('vehicle_detail', listing_id=listing.id)
            
#         bid_amount = float(request.POST.get("bid_amount", 0))
        
#         return redirect('vehicle', listing_id=listing.id)



def place_bid(request, listing_id):
    print("--- 🚀 PLACE BID VIEW TRIGGERED ---") # Track 1
    
    if request.method == "POST":
        bid_amount_raw = request.POST.get('bid_amount')
        print(f"📥 Raw input received from HTML form: {bid_amount_raw}") # Track 2
        
        try:
            # Check if converting to a float or decimal works
            bid_amount = float(bid_amount_raw)
            print(f"🔢 Converted bid amount to number: {bid_amount}") # Track 3
        except (TypeError, ValueError):
            print("❌ CRITICAL: Failed to convert bid_amount to a valid number!")
            # If this prints, your HTML form is sending empty or broken data

        listing = get_object_or_404(Listing, id=listing_id)
        print(f"🚘 Current Listing Price in DB: {listing.current_price}") # Track 4

        # Check the logic gate
        if bid_amount > float(listing.current_price):
            print("✅ SUCCESS: New bid is higher than current price. Saving...") # Track 5
            
            # ... your code that saves the bid and updates listing.current_price ...
            
            print(f"💾 DB Updated! New current price is: {listing.current_price}")
        else:
            print("❌ FAILURE: Bid was NOT higher than current price. Skipping save!") # Track 6

    print("↩️ Redirecting back to vehicle page...") # Track 7
    return redirect('vehicle', listing_id=listing_id)

