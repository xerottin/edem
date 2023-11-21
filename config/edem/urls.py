from django.urls import path
from . import views

urlpatterns = (
    path('', views.index, name='index'),
    path('rooms/<int:pk>', views.rooms, name='rooms'),
)
