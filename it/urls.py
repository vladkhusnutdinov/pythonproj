from django.urls import path
from .views import *

urlpatterns = [
    path('', main), #http://127.0.0.1:8000/
    path('demand/', demand), #http://127.0.0.1:8000/
    path('geo/', geo),
    path('main/', main)
]
