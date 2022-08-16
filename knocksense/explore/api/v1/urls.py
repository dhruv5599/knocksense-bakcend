from django.urls import path
from .views import NewsList, TagList

 
urlpatterns = [
    path('',NewsList.as_view()),
    path('<int:pk>/',NewsList.as_view()),
    path('tag/',TagList.as_view()),
    path('tag/<int:pk>/',TagList.as_view()),

]
