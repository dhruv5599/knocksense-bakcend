from django.urls import path
from .views import NewsList

 
urlpatterns = [
    path('',NewsList.as_view()),
    path('<int:pk>/',NewsList.as_view()),

]
