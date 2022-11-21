from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', log_in, name='login'),
    path('your_profile/', profile, name='profile'),
    path('change_password/', change_password, name='change_password'),
    path('logout/', logout_view, name='logout'),
    path('verify/<int:id>/', verify, name='verify'),
    path('resend/<int:id>/', resend_code, name='resend'),
]