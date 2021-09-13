from django.urls import path
from .views import *

app_name = "users_auth"

urlpatterns = [
    path('userpage/', userpage, name="userpage"),
    path('login/', login_profile, name="login"),
    path('logout/', logout_profile, name='logout'),
    path('register_profile/', register_profile, name='register_profile'),
]
