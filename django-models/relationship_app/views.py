from django.shortcuts import render

# Create your views here.

from .models import Book

def book_list(request):
      books = Book.objects.all()
      context = {'book_list': books}
      return render(request, "relationship_app/list_books.html", context)