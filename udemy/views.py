from django.shortcuts import render
from django.views.generic import ListView

from courses.models import Course, Category


def index(request):
    return render(request, 'index.html', {})


class HomeListView(ListView):
    model = Course
    template_name = 'index.html'
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['top_courses'] = self.model.objects.all().order_by('?')
        return context
