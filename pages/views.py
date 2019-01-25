from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices,bedroom_choices,state_choices
from listings.models import Listing

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
    'listings': listings,
    'price_choices': price_choices,
    'bedroom_choices': bedroom_choices,
    'state_choices': state_choices,
    }
    return render(request, 'pages/index.html',context)

def about(request):
    listings = Listing.objects.all()
    context = {
    'listings': listings,
    }
    return render(request, 'pages/about.html', context)
