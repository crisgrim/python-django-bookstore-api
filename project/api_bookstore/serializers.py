from rest_framework import serializers
from .models import Author, Book
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    added_by = UserSerializer()

    class Meta:
        model = Author
        fields = ('name', 'added_by', 'created_date')


class BookSerializer(serializers.HyperlinkedModelSerializer):
    added_by = UserSerializer()

    class Meta:
        model = Book
        fields = ('title', 'description', 'author', 'added_by', 'created_date')
