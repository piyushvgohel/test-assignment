from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from dogs.models import Breed, Dog

from dogs.serializers import BreedSerializer, DogSerializer


# Create your views here.


class BreedList(APIView):

    def get(self, request, format=None):
        breeds = Breed.objects.all()
        serializer = BreedSerializer(breeds, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = BreedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BreedDetail(APIView):

    def get_object(self, pk):
        try:
            return Breed.objects.get(pk=pk)
        except Breed.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        breed = self.get_object(pk)
        serializer = BreedSerializer(breed)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        breed = self.get_object(pk)
        serializer = BreedSerializer(breed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        breed = self.get_object(pk)
        breed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DogList(APIView):

    def get(self, request, format=None):
        dogs = Dog.objects.all()
        dog_serializer = DogSerializer(dogs, many=True)
        return Response(dog_serializer.data)


    def post(self, request, format=None):
        dog_serializer = DogSerializer(data=request.data)
        if dog_serializer.is_valid():
            dog_serializer.save()
            return Response(dog_serializer.data, status=status.HTTP_201_CREATED)
        return Response(dog_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DogDetail(APIView):

    def get_object(self, pk):
        try:
            return Dog.objects.get(pk=pk)
        except Dog.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        dog_obj = self.get_object(pk)
        dog_serializer = DogSerializer(dog_obj)
        return Response(dog_serializer.data)

    def put(self, request, pk, format=None):
        dog_obj = self.get_object(pk)
        dog_serializer = DogSerializer(dog_obj, data=request.data)
        if dog_serializer.is_valid():
            dog_serializer.save()
            return Response(dog_serializer.data)
        return Response(dog_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dog_obj = self.get_object(pk)
        dog_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)