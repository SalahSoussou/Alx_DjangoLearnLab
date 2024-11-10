from django.shortcuts import render

# Create your views here.

from .models import Book
from .models import Library
from django.views.generic.detail import DetailView

def book_list(request):
      books = Book.objects.all()
      context = {'book_list': books}
      return render(request, "relationship_app/list_books.html", context)




class LibraryDetailView(DetailView):
  model = Library
  template_name = "relationship_app/library_detail.html"