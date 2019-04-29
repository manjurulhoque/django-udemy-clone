from django.urls import path
from .views import *

app_name = 'courses'

urlpatterns = [
    path('courses/<slug:slug>', CourseDetailView.as_view(), name='course-details'),
    path('courses/<slug:slug>/category', CoursesByCategoryListView.as_view(), name='course-by-category'),
]
