from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.utils import timezone
from .models import Listing


@login_required
def upload(request):
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

def list_view(request):
    listings = Listing.objects.all()
    return render(request, "listings/index.html", {"listings": listings})


# show on home page
def home(request):
    listings = Listing.objects.all()
    return render(request, "index.html", {"listings": listings})

# vehicle detail page request
def vehicle_detail(request, listing_id):
    listing = get_object_or_404(Listing, id=listing_id)
    return render(request, 'vehicle.html', {'listing': listing})


# from my listing edit modal 
def edit_listing(request):
    
    if request.method == "POST":

        # id from edit form
        listing_id = request.POST.get("listing_id")
        # fetch records
        listing = get_object_or_404(Listing, id=listing_id)

        listing.make = request.POST.get("make")
        listing.model = request.POST.get("model")
        listing.year = request.POST.get("year")
        listing.registration = request.POST.get("registration")
        listing.mileage = request.POST.get("mileage")
        listing.fuel = request.POST.get("fuel")
        listing.transmission = request.POST.get("transmission")
        listing.condition = request.POST.get("condition")
        listing.colour = request.POST.get("colour")
        listing.doors = request.POST.get("doors")
        listing.description = request.POST.get("description")
        listing.starting_price = request.POST.get("starting_price")
        listing.reserve_price = request.POST.get("reserve_price")

        end_date = request.POST.get("end_date")
        end_time = request.POST.get("end_time")
        if end_date and end_time:
            ends_at_str = f"{end_date} {end_time}"
            ends_at = datetime.strptime(ends_at_str, "%Y-%m-%d %H:%M")
            listing.ends_at = timezone.make_aware(ends_at)

        if request.FILES.get("image1"):
            listing.image1 = request.FILES.get("image1")
        if request.FILES.get("image2"):
            listing.image2 = request.FILES.get("image2")
        if request.FILES.get("image3"):
            listing.image3 = request.FILES.get("image3")
        if request.FILES.get("image4"):
            listing.image4 = request.FILES.get("image4")

        listing.save()
        return redirect('my_listings')

