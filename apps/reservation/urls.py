from django.urls import path
from apps.reservation.views import RequestedReservationsListView, ReservationCreateView

urlpatterns = [
    path('request_service/<int:pk>/', ReservationCreateView.as_view(), name='request_service'),
    path('reservations/', RequestedReservationsListView.as_view(), name='reservations'),
]
