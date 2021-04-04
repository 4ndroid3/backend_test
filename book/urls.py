""" Book URLS"""
# Django Imports
from django.urls import path, include

# Django REST Framework Imports
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

# Project Imports
from book import views

router = DefaultRouter()
router.register(r'library', views.LibraryView, basename='library')
router.register(
    r'library/(?P<libraries_pk>[^/.]+)/books',
    views.LibraryBookView,
    basename='library_books')
router.register(r'book', views.BookView, basename='book')
router.register(r'author', views.AuthorView, basename='author')
router.register(r'lead', views.LeadView, basename='lead')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
