""" Books Serializers"""

# Django REST Framework Imports
from rest_framework import serializers

# Django Imports
from django.core.mail import send_mail

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
    """ Serializer para crear un Lead"""

    def create(self, validated_data):
        ModelClass = self.Meta.model
        instance = ModelClass._default_manager.create(**validated_data)
        send_mail(
            'Confirmación', 
            'Hola {} su compra fue realizada'.format(validated_data['full_name']),
            'me@gmail.com',
            [validated_data['email']],
        )

        return instance

    class Meta:
        """ Meta Class"""
        model = Leads
        fields = ('email', 'full_name', 'phone', 'library')
