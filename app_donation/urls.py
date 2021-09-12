from django.urls import path
from .views import *

app_name = 'app_donation'

urlpatterns = [
    path('search_rc/', search_rc, name="search_rc"),
    path('customer_service/<id>/', customer_service, name="customer_service"),
    path('confirm_ca/<id>/', confirm_ca, name='confirm_ca'),
]
