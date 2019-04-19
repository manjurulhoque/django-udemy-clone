from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'udemy'

urlpatterns = [
    path('', index, name='home'),
]
