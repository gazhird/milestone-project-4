from django.shortcuts import render

# render pages 
def home(request):
    return render(request, 'index.html')

def upload(request):
    return render(request, 'my_listings.html')


