from django.urls import path
from .views import payments_success, checkout, billing_info, process_order


urlpatterns = [
    path('payments-success', payments_success, name='payments_success'),
    path('checkout', checkout, name='checkout'),
    path('billing_info', billing_info, name="billing_info"),
    path('process_order', process_order, name="process_order")
]