from django.urls import path
from . import views

urlpatterns = [
    path("",views.createRoom,name='createRoom'),
    path("create",views.createRoom,name='createRoom'),
    path("room/<str:pk>",views.room, name="room"),
    path("submit/<str:pk>",views.submit, name="submit"),
    path("GetMessages/<str:pk>",views.GetMessage),
    path("adminPanel",views.adminPanel),
    path("adminPanel_search",views.adminPanel_search),
    
]
