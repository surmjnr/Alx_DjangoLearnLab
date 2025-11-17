from django.db import models


class Author(models.Model):
	"""Model representing an Author"""
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Book(models.Model):
	"""Model representing a Book"""
	title = models.CharField(max_length=200)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)

	def __str__(self):
		return self.title


class Library(models.Model):
	"""Model representing a Library"""
	name = models.CharField(max_length=150)
	books = models.ManyToManyField(Book)

	def __str__(self):
		return self.name


class Librarian(models.Model):
	"""Model representing a Librarian"""
	name = models.CharField(max_length=100)
	library = models.OneToOneField(Library, on_delete=models.CASCADE)

	def __str__(self):
		return self.name
