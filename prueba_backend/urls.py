"""URLS Cofiguration"""

# Django Imports
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('book.urls')),
    
    # path(
    #     route = 'library/{id}',
    #     view = views.LibraryView,
    #     name = 'library_ABM',
    # ),
    # path(
    #     route = 'library/{id}/books/{id}',
    #     view = ,
    #     name = 'librery_filter',
    # ),
    # path(
    #     route = 'book/{id}', 
    #     view = ,
    #     name = 'book_ABM',
    # ),
    # path(
    #     route = 'book/search?text="{title}"',
    #     view = ,
    #     name = 'book_search',    
    # ),
    # path(
    #     route = 'author/{id}',
    #     view = ,
    #     name = 'author',    
    # ),
    # path(
    #     route = 'lead/',
    #     view = ,
    #     name = 'leads',    
    # ),

]
