""" Book Views"""

# Django REST Framework Imports
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import mixins
from rest_framework import filters

# Project Imports
from book.serializers import *
from .models import Book, Author, Library, Leads

class LibraryView(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin, GenericViewSet):
    """ View de library, realiza acciones de ABM"""
    queryset = Library.objects.all()
    serializer_class = LibraryModelSerializer


class LibraryBookView(mixins.RetrieveModelMixin,
                      GenericViewSet):
    """ View para filtrar entre librerias 
    y los libros que contienen cada una """
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    def get_queryset(self):
        queryset = Book.objects.filter(libraries = self.kwargs['libraries_pk'])

        return queryset

class BookView(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin, mixins.ListModelMixin,
                GenericViewSet):

    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ['$title',]

    