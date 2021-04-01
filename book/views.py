""" Book Views"""

# Django REST Framework Imports
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

# Project Imports
from book.serializers import *

# from django.views.generic import ListView, CreateView
# from django.views.generic.edit import CreateView

from .models import Book, Author, Library, Leads


# class BookListView(ListView):
#     paginate_by = 100
#     model = Book
#     context_object_name = 'books'

#     def get_queryset(self):
#         qs = super(BookListView, self).get_queryset()
#         qs.order_by('title')
#         return qs


# class AuthorListView(ListView):
#     paginate_by = 100
#     model = Author
#     context_object_name = 'authors'


# class LibraryListView(ListView):
#     paginate_by = 10
#     model = Library
#     context_object_name = 'libraries'

# class LeadsCreationView(CreateView):
#     pass

# book_list_view = BookListView.as_view()
# author_list_view = AuthorListView.as_view()
# library_list_view = LibraryListView.as_view()
# leads_create_view = LeadsCreationView.as_view()

class LibraryView(ModelViewSet):
    """ View de library, realiza acciones de ABM"""
    queryset = Library.objects.all()
    serializer_class = LibraryModelSerializer

