from django.urls import path
from apps.reservation.views import MakeReservationsView

urlpatterns = [
    path('new/', MakeReservationsView.as_view(), name='reservation_new'),
]
