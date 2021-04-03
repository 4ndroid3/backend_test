"""URLS Cofiguration"""

# Django REST Framework Imports
from rest_framework_simplejwt import views as jwt_views

# Django Imports
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('book.urls')),
]