from django.shortcuts import render, get_object_or_404
from .models import Course, Photo
from .forms import PhotoForm


# Create your views here.
def index(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {
        'courses': courses,
    })


def rooms(request, pk):
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
        'course': course,
        'photos': photos,
        'form': form,
    })
