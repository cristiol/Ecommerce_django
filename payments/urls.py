from django.urls import path
from .views import payments_success


urlpatterns = [
    path('payments-success', payments_success, name='payments_success')
]