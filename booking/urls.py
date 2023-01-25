from django.urls import path

from accounts.views import my_view
from .views import*


urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('bookings/<int:pk>', bookings, name='bookings'),
    path('book/<int:pk>', BookRoomView.as_view(), name='book')
]