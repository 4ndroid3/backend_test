"""URLS Cofiguration"""

# Django Imports
from django.contrib import admin
from django.urls import path

# Project Imports
from book import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        route = '',
        view = book_list_view,
        name = '',
    ),

    path(
        route = '',
        author_list_view,
        name = '',
    ),
    path(
        route = '', 
        view = library_list_view,
        name = '',
    ),
    path(
        route = '',
        view = leads_create_view,
        name = '',    
    ),

]
