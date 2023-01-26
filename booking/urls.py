from django.urls import path

from accounts.views import register, signin, signout
from .views import*


urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('bookings/<int:pk>', bookings, name='bookings'),
    path('book/<int:pk>', BookRoomView.as_view(), name='book'),
    path('register/', register, name='register'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout')
]