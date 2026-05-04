from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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
        ends_at = request.POST.get("ends_at")

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

        return redirect("listings:list")

    return render(request, "upload.html")