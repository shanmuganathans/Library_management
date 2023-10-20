# library_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_book, name='add_book'),
    path('display/', views.display_books, name='display_books'),
    path('delete/<str:isbn>/', views.delete_book, name='delete_book'),
    path('edit/<str:isbn>/', views.edit_book, name='edit_book'),
]
