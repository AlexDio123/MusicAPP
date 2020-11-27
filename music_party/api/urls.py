from django.urls import path, include
from .views import RoomView, CreateRoomView, GetRoom

urlpatterns = [
    path('', include('frontend.urls')),
    path('room', RoomView.as_view(), name="room"),
    path('create-room', CreateRoomView.as_view()),
    path('get-room', GetRoom.as_view()),
]