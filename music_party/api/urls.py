from django.urls import path, include
from .views import RoomView

urlpatterns = [
    path('', include('frontend.urls')),
    path('room', RoomView.as_view(), name="room"),
]