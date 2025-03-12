from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Notes

# this is for user authentication
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User # this is the model that we are going to serialize
        fields = ['id', 'username', 'email', 'password'] # these are the fields that we want to serialize when we are accepting and returning a new user
        extra_kwargs = {'password': {'write_only': True}} # this is for the password field, we want to make sure that the password is write only and required

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ['id', 'title', 'content', 'created_at', 'author'] # these are the fields that we want to serialize when we are accepting and returning a new note
        extra_kwargs = {'author': {'read_only': True}}
    def create(self, validated_data):
        note = Notes.objects.create(author=self.context['request'].user, **validated_data)
        return note