from django.db import models

# Create your models here.

# class Author(models.Model):
#     name = models.CharField(max_length=255)


# class Book(models.Model):
#     title = models.CharField( max_length=50)
#     publication_year = models.DateField()
#     author = models.ManyToOneRel(field='ForeignKey'  ,to= Author, field_name='name',)



class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title