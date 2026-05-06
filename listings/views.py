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
        end_date = request.POST.get("end_date")  # e.g. "2026-05-22"
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

    return render(request, "upload.html")

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
    return render(request, 'listings/vehicle.html', {'listing': listing})
