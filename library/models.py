from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    descr = models.TextField(blank=True, default="")

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Department(name={self.name})"


class Author(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"Author(name={self.name})"


class Publisher(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100, help_text="complete title of the book")
    author = models.ManyToManyField("Author", related_name='books')
    dept = models.ManyToManyField("Department", related_name='books')
    copies = models.PositiveIntegerField(blank=True, default=1)
    edition = models.PositiveIntegerField(blank=True, null=True)
    publisher = models.ForeignKey("Publisher", on_delete=models.CASCADE, blank=True, null=True, related_name='books')
    cover_image = models.ImageField(upload_to="book_covers/" , default="/default_cover.png")
    data = models.FileField(upload_to="books/", blank=True, null=True)

    def __str__(self):
        return self.title

