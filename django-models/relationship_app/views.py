from django.shortcuts import render

# Create your views here.

from .models import Library

def book_list(request):
      books = Library.objects.all()
      context = {'book_list': books}
      return render(request, "relationship_app/list_books.html", context)

"relationship_app/library_detail.html"