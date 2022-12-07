from django.shortcuts import render
from django.http import HttpResponseRedirect
from . models import Mymodel
from . models import BookingItems
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.
import requests

def index(request):
    return render(request, 'index.html')

def booking_view(request):
    all_booking_items=BookingItems.object.all()
    return render(request, 'index.html',{'all_items': all_booking_items})
    
@login_required(login_url='/login')
def flightbooking(request):
	
    booking=Post()
    booking.travelling_from=request.POST.get('travelling_from')
    booking.travelling_to=request.POST.get('travelling_to')
    booking.date_of_travelling=request.POST.get('date_of_travelling')
    booking.number_of_passengers=request.POST.get('number_of_passengers')
    booking.save()
    return HttpResponseRedirect('/book/')

class CreateMyModelView():
    model = Mymodel
    template_name = 'ticket_app/index.html'
    success_url = 'ticket_app/booking.html'