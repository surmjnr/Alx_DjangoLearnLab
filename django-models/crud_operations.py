#!/usr/bin/env python
"""
CRUD Operations Script for Book Model
"""

import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from bookshelf.models import Book

print("=" * 60)
print("DJANGO CRUD OPERATIONS FOR BOOK MODEL")
print("=" * 60)
print()

# CREATE: Create a Book instance
print("CREATE OPERATION:")
print("-" * 60)
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(f"Command: Book.objects.create(title='1984', author='George Orwell', publication_year=1949)")
print(f"Output: Book created successfully with ID {book.id}")
print(f"  - Title: {book.title}")
print(f"  - Author: {book.author}")
print(f"  - Publication Year: {book.publication_year}")
print()

# RETRIEVE: Get the book
print("RETRIEVE OPERATION:")
print("-" * 60)
retrieved_book = Book.objects.get(id=book.id)
print(f"Command: Book.objects.get(id={book.id})")
print(f"Output: Book retrieved successfully")
print(f"  - Title: {retrieved_book.title}")
print(f"  - Author: {retrieved_book.author}")
print(f"  - Publication Year: {retrieved_book.publication_year}")
print(f"  - ID: {retrieved_book.id}")
print()

# UPDATE: Update the title
print("UPDATE OPERATION:")
print("-" * 60)
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
print(f"Command: book.title = 'Nineteen Eighty-Four'; book.save()")
print(f"Output: Book updated successfully")
updated_book = Book.objects.get(id=book.id)
print(f"Verification: Title is now '{updated_book.title}'")
print()

# DELETE: Delete the book
print("DELETE OPERATION:")
print("-" * 60)
book_id = retrieved_book.id
retrieved_book.delete()
print(f"Command: book.delete()")
print(f"Output: Book with ID {book_id} deleted successfully")
remaining_books = Book.objects.all()
print(f"Verification: Remaining books in database: {list(remaining_books)}")
print(f"Total books after deletion: {remaining_books.count()}")
print()

print("=" * 60)
print("CRUD OPERATIONS COMPLETED SUCCESSFULLY")
print("=" * 60)
