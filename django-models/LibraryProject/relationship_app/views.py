# from django.shortcuts import render
# from django.contrib.auth import login
# from django.contrib.auth.forms import UserCreationForm

# # Create your views here.

# from .models import Book
# from .models import Library
# from django.views.generic.detail import DetailView

# def book_list(request):
#       books = Book.objects.all()
#       context = {'book_list': books}
#       return render(request, "relationship_app/list_books.html", context)




# class LibraryDetailView(DetailView):
#   model = Library
#   template_name = "relationship_app/library_detail.html"


# "from django.contrib.auth.decorators import permission_required", "relationship_app.can_add_book", "relationship_app.can_change_book", "relationship_app.can_delete_book"

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, HttpResponse

def check_role(role):
    def decorator(user):
        return user.is_authenticated and user.userprofile.role == role
    return decorator

@user_passes_test(check_role('Admin'))
def admin_view(request):
    return HttpResponse("This is the Admin view.")

@user_passes_test(check_role('Librarian'))
def librarian_view(request):
    return HttpResponse("This is the Librarian view.")

@user_passes_test(check_role('Member'))
def member_view(request):
    return HttpResponse("This is the Member view.")
"relationship_app/register.html"
"from django.contrib.auth.decorators import permission_required", "relationship_app.can_add_book", "relationship_app.can_change_book", "relationship_app.can_delete_book"