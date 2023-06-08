
from apps.reservation.forms import ReservationForm
from django.urls import reverse_lazy

from django.views.generic.list import ListView
from .models import Reservation

from django.views.generic.edit import UpdateView

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from .models import Reservation
from apps.posts.models import Post
from apps.dog.models import Dog


""" Funcion para la solicitud """
@method_decorator(login_required, name='dispatch')
class ReservationCreateView(View):
    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        dog_id = request.POST.get('dog')
        dog = get_object_or_404(Dog, pk=dog_id)
        Reservation.objects.create(
            sitter=post.user,
            owner=request.user,
            start_date = request.POST.get('start_date'),
            end_date = request.POST.get('end_date'),
            dog=dog,  # Aquí usamos la mascota seleccionada por el usuario
            status='S'  # El estado inicial es 'Solicitada'
        )
        return redirect('post_list')



""" Vista para ver las reservaciones solicitadas (CUIDADOR) """
class RequestedReservationsListView(ListView):
    model = Reservation
    template_name = 'reservation/requested_reservations.html'

    def get_queryset(self):
        return Reservation.objects.filter(sitter=self.request.user, status='S')



""" Vistas de Aceptación/Rechazo de Reservaciones (CUIDADOR) """
class ReservationResponseView(UpdateView):
    model = Reservation
    fields = ['status']

    def form_valid(self, form):
        # Solo se puede responder a las reservaciones que están en estado 'Solicitada'
        if self.object.status != 'S':
            return redirect('nombre_de_tu_vista_de_error')

        return super().form_valid(form)

class ReservationAcceptView(ReservationResponseView):
    def form_valid(self, form):
        form.instance.status = 'A'
        return super().form_valid(form)

class ReservationRejectView(ReservationResponseView):
    def form_valid(self, form):
        form.instance.status = 'R'
        return super().form_valid(form)



