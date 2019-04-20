from django.contrib import admin

from .models import Category, Course, Lesson


class CourseAdmin(admin.ModelAdmin):
    exclude = ('slug',)


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('slug',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
