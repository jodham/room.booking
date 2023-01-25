from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import BookingForm
from .models import *


# Create your views here.
def index(request):
    templatename = 'booking/index.html'
    context = {}
    return render(request, templatename, context)


def dashboard(request):
    templatename = 'booking/dashboard.html'
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, templatename, context)


# def book(request, pk):
#     room = Room.objects.get(id=pk)
#     user = request.user
#
#     if request.method == 'POST':
#         user = user
#         room = request.POST.get("room_id")
#         total_users = request.POST.get("no_of_users")
#         starting_time = request.POST.get("starttime")
#         endingtime = request.POST.get("endtime")
#
#         x = Boooking()
#         x.user = user
#         x.room_id = room
#         x.no_of_users = total_users
#         x.start_time = starting_time
#         x.end_time = endingtime
#         x.save()
#
#     templatename = 'booking/book_room_form.html'
#     context = {'room': room, 'user': user}
#     return render(request, templatename, context)

class BookRoomView(CreateView):
    model = Boooking
    template_name = 'booking/book_room_form.html'
    form_class = BookingForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        room = Room.objects.get(id=self.kwargs['pk'])
        form.instance.room = room
        return super().form_valid(form)


def bookings(request, pk):
    books = Boooking.objects.filter(Q(room_id=pk))
    room = Room.objects.get(id=pk)
    room_no = room.id
    templatename = 'booking/bookings.html'
    context = {'books': books, 'room_no': room_no}
    return render(request, templatename, context)
