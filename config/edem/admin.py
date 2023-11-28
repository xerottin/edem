# admin.py

from django.contrib import admin
from .models import Course, Photo


class PhotoInline(admin.StackedInline):  # или admin.TabularInline для более компактного отображения
    model = Photo
    extra = 1  # количество дополнительных форм для добавления фотографий


class CourseAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]


admin.site.register(Course, CourseAdmin)
admin.site.register(Photo)
