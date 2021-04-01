""" Books Serializers"""

# Django Imports
from .models import Book, Author, Library, Leads

# Django REST Framework Imports
from rest_framework import serializers

# Project Imports

class LibraryModelSerializer(serializers.ModelSerializer):
    """Serializer para las librerias"""
    
    class Meta:
        """Meta Class"""

        model = Library
        fields = ('name',)