""" Book Views"""

# Django REST Framework Imports
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Project Imports
from book.serializers import (
    LibraryModelSerializer,
    BookModelSerializer,
    AuthorModelSerializer,
    LeadModelSerializer)

from .models import Book, Author, Library, Leads


class LibraryView(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin, GenericViewSet):
    """ View de library, realiza acciones de ABM
    Para realizar """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Library.objects.all()
    serializer_class = LibraryModelSerializer


class LibraryBookView(mixins.RetrieveModelMixin,
                      GenericViewSet):
    """ View para filtrar entre librerias 
    y los libros que contienen cada una """
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    def get_queryset(self):
        """ Se filtra a los libros por librerias, solo dara 
        resultados que coincidan, libros adentro de librerias """
        queryset = Book.objects.filter(libraries=self.kwargs['libraries_pk'])

        return queryset


class BookView(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin, mixins.ListModelMixin,
               GenericViewSet):
    """ View de book, realiza acciones de ABM,
    hace filtro de busqueda de los titulos de libros """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    # Agrego filtros de busquedas
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = ['$title', ]
    filter_fields = ['title', 'author', 'libraries']


class AuthorView(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin, GenericViewSet):
    """ View de authors, realiza acciones de ABM """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


class LeadView(mixins.CreateModelMixin, GenericViewSet):
    """ View de leads, crea un lead y envia un email al usuario del email"""
    queryset = Leads.objects.all()
    serializer_class = LeadModelSerializer
