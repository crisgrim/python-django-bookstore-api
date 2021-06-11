from django.shortcuts import render
from rest_framework import viewsets

from .serializers import AuthorSerializer, BookSerializer, UserSerializer
from .models import Author, Book
from django.contrib.auth.models import User

# Create your views here.


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('name')
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_fields = ['username']
