from django.shortcuts import render
# since we have a user in serializers.py, views are needed, it allows to make use of the user model
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Notes

# Create your views here.
# next thing is to create a class based view that will allow to implement creating a new user, its kinda like a registeration form

# creating a view for creating a new note
class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated] # this is to make sure that only authenticated users can create a new note


    def get_queryset(self):
        user = self.request.user
        return Notes.objects.filter(author=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)
            return serializer.errors


# for deleting a note
class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated] # this is to make sure that only authenticated users can delete a note
    def get_queryset(self):
        user = self.request.user
        return Notes.objects.filter(author=user)

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny] # this is to allow anyone to create a user