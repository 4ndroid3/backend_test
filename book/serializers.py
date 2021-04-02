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

class AuthorModelSerializer(serializers.ModelSerializer):
    """ Serializer de Authors"""
    class Meta:
        """ Meta Class"""
        model = Author
        fields = ('first_name', 'last_name')

class LeadModelSerializer(serializers.ModelSerializer):
    """ Serializer de Leads"""
    class Meta:
        """ Meta Class"""
        model = Leads
        fields = ('email', 'full_name', 'phone', 'library')