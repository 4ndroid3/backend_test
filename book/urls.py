""" Book URLS"""
# Django Imports
from django.urls import path, include

# Django REST Framework Imports
from rest_framework.routers import DefaultRouter

# Project Imports
from book import views

router = DefaultRouter()
router.register(r'library', views.LibraryView, basename = 'library')


urlpatterns = [
    path('', include(router.urls)),
]