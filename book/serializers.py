""" Books Serializers"""

# Django REST Framework Imports
from rest_framework import serializers

# Project Imports
from .models import Book, Author, Library, Leads

class LibraryModelSerializer(serializers.ModelSerializer):
    """Serializer para las librerias"""
    
    class Meta:
        """Meta Class"""

        model = Library
        fields = ('name',)

class BookModelSerializer(serializers.ModelSerializer):
    """ Serializer de books"""
    class Meta:
        """ Meta Class"""
        model = Book
        fields = ('title', 'author', 'libraries',)