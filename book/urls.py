""" Book URLS"""
# Django Imports
from django.urls import path, include

# Django REST Framework Imports
from rest_framework.routers import DefaultRouter

# Project Imports
from book import views

router = DefaultRouter()
router.register(r'library', views.LibraryView, basename = 'library')
router.register(
    r'library/(?P<libraries_pk>[^/.]+)/books',
    views.LibraryBookView,
    basename = 'library_books')
router.register(r'book', views.BookView, basename = 'book')

urlpatterns = [
    path('', include(router.urls)),
]
