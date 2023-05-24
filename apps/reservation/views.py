from django.shortcuts import render
from django.views.generic import CreateView
from apps.reservation.models import Reservation
from apps.reservation.forms import ReservationForm
from django.urls import reverse_lazy
# Create your views here.
class MakeReservationsView(CreateView):
  model = Reservation
  form_class = ReservationForm
  template_name = 'reservation/new.html'
  success_url = reverse_lazy('reservation_new')
  