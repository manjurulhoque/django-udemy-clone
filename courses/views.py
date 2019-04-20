from django.shortcuts import render
from django.views.generic import DetailView

from courses.models import Course


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/details.html'
    context_object_name = 'course'
