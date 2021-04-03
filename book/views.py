""" Book Views"""

# Django REST Framework Imports
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import ListCreateAPIView
from rest_framework import mixins
from rest_framework import filters

from rest_framework_simplejwt.views import TokenObtainPairView

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
        """ Se filtra a los libros por librerias, solo dara 
        resultados que coincidan, libros adentro de librerias """
        queryset = Book.objects.filter(libraries = self.kwargs['libraries_pk'])

        return queryset

class BookView(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin, mixins.ListModelMixin,
                GenericViewSet):
    """ View de book, realiza acciones de ABM,
    hace filtro de busqueda de los titulos de libros """
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ['$title',]

class AuthorView(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin, GenericViewSet):
    """ View de authors, realiza acciones de ABM """
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer

class LeadView(mixins.CreateModelMixin, GenericViewSet):
    """ View de leads, crea un lead y envia un email al usuario del email"""
    queryset = Leads.objects.all()
    serializer_class = LeadModelSerializer

