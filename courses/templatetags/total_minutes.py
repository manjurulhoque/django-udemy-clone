from django import template
from django.db.models import Sum, Avg, Max, Min, Count

register = template.Library()


@register.filter
def total_minutes(queryset):
    return queryset.aggregate(Sum('duration')).get('duration__sum')
