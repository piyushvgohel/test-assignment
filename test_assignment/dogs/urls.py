from django.urls import path
from dogs.views import BreedList, BreedDetail, DogList, DogDetail

urlpatterns = [
    path('breeds/', BreedList.as_view()),
    path('breeds/<uuid:pk>/', BreedDetail.as_view()),
    path('dogs/', DogList.as_view()),
    path('dogs/<uuid:pk>/', DogDetail.as_view()),
]