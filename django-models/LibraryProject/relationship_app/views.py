from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

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


"from django.contrib.auth.decorators import permission_required", "relationship_app.can_add_book", "relationship_app.can_change_book", "relationship_app.can_delete_book"