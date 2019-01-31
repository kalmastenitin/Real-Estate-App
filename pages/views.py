from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices,bedroom_choices,state_choices
from listings.models import Listing
from django.contrib import messages
from django.core.mail import send_mail

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

def contact(request):
    if request.method == 'POST':        
        name = request.POST.get('name')
        contact_num = request.POST.get('number')
        email_id = request.POST.get('email')
        inquiry_asked = request.POST.get('message')
        #send_mail
        send_mail(
            'Real Estate Site Enquiry',
            inquiry_asked,
            'nknckalmaste@gmail.com',
            [email_id ],
            fail_silently=False
        )

    return render(request, 'pages/contact.html')
