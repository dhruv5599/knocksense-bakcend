
from django.urls import path
from .views import UserList, AutherList


urlpatterns = [
    path('',UserList.as_view()),
    path('<int:pk>/',UserList.as_view()),
    path('author/',AutherList.as_view()),
    path('author/<int:pk>/',AutherList.as_view()),
]