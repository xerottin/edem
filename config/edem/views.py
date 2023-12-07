from django.shortcuts import render, get_object_or_404
from .models import Course, Photo
from .forms import PhotoForm


def index(request):
    button = False
    is_succes = True
    courses = Course.objects.all()
    return render(request, 'index.html', {
        'button': button,
        'is_succes': is_succes,
        'courses': courses,
    })


def rooms(request, pk):
    button = True
    is_succes = False
    course = get_object_or_404(Course, pk=pk)
    photos = Photo.objects.filter(course=course)

    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.course = course
            photo.save()
    else:
        form = PhotoForm()

    return render(request, 'rooms.html', {
        'button': button,
        'is_succes': is_succes,
        'course': course,
        'photos': photos,
        'form': form,
    })


def album(request):
    button = True
    is_succes = False
    return render(request, 'album.html', {
        'is_succes': is_succes,
        'button': button,
    })
