from django.urls import path

from accounts.views import my_view
from .views import*


urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard')
]