from django.shortcuts import render, get_object_or_404

from edem.models import Rooms


# Create your views here.
def index(request):
    room = get_object_or_404(Rooms)
    return render(request, 'index.html', {
        rooms: 'rooms',
    })


def rooms(request):
    return render(request, 'rooms.html')
