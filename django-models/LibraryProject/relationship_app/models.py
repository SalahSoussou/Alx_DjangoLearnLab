from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200)



class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book)

class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

"return self.name"
"class UserProfile(models.Model):", "Admin", "Member"
"class Meta", "permissions"
"can_add_book", "can_change_book", "can_delete_book"