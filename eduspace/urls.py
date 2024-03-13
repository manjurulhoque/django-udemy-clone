from django.urls import path
from .views import *

app_name = 'eduspace'

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('search', SearchView.as_view(), name='search'),
]
