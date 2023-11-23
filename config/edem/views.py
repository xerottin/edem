from .models import Course, Photo
from django.shortcuts import render


# Create your views here.
def index(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {
        'courses': courses,
    })


def rooms(request, pk):
    obj = Photo.objects.get(pk=4)
    image_paths = obj.get_images()
    course = Course.objects.get(pk=pk)
    return render(request, 'rooms.html', {
        'course': course,
        'image_paths': image_paths
    })
