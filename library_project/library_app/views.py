# library_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from .models import Book
from .forms import BookForm

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_books')
    else:
        form = BookForm()
    return render(request, 'library_app/add_book.html', {'form': form})

def display_books(request):
    books = Book.objects.all()
    return render(request, 'library_app/display_books.html', {'books': books})

def delete_book(request, isbn):
    try:
        book = get_object_or_404(Book, isbn=isbn)
        book.delete()
    except ObjectDoesNotExist:
        pass
    return redirect('display_books')

def edit_book(request, isbn):
    book = get_object_or_404(Book, isbn=isbn)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('display_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'library_app/edit_book.html', {'form': form})
