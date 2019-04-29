from django.http import Http404
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from courses.models import Course, Category


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/details.html'
    context_object_name = 'course'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        slug = self.kwargs.get(self.slug_url_kwarg)
        slug_field = self.get_slug_field()
        queryset = queryset.filter(**{slug_field: slug})
        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404("No %(verbose_name)s found matching the query" %
                          {'verbose_name': self.model._meta.verbose_name})
        return obj


class CoursesByCategoryListView(ListView):
    model = Course
    template_name = 'courses/courses_by_category.html'
    context_object_name = 'courses'

    def get_queryset(self):
        category = Category.objects.get(slug=self.kwargs['slug'])
        return self.model.objects.filter(category_id=category.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.objects.get(slug=self.kwargs['slug'])
        context['category'] = category
        context['categories'] = Category.objects.all()
        return context
