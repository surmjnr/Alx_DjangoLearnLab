"""
Sample queries demonstrating relationships between entities in the relationship_app.

This script contains example queries for:
1. Query all books by a specific author
2. List all books in a library
3. Retrieve the librarian for a library
"""

from relationship_app.models import Author, Book, Library, Librarian


def query_books_by_author(author_id):
    """
    Query all books written by a specific author.
    
    Args:
        author_id (int): The ID of the author
    
    Returns:
        QuerySet: All books by the specified author
    """
    author = Author.objects.get(id=author_id)
    books = Book.objects.filter(author=author)
    return books


def query_books_in_library(library_id):
    """
    List all books available in a specific library.
    
    Args:
        library_id (int): The ID of the library
    
    Returns:
        QuerySet: All books in the specified library
    """
    library = Library.objects.get(id=library_id)
    books = library.books.all()
    return books


def query_librarian_for_library(library_id):
    """
    Retrieve the librarian assigned to a specific library.
    
    Args:
        library_id (int): The ID of the library
    
    Returns:
        Librarian: The librarian for the specified library
    """
    librarian = Librarian.objects.get(library_id=library_id)
    return librarian


# Example usage and testing queries
if __name__ == "__main__":
    # Note: These examples assume you have data in your database
    
    # Example 1: Query all books by a specific author
    print("=" * 60)
    print("Example 1: Query all books by a specific author")
    print("=" * 60)
    try:
        author_id = 1
        books_by_author = query_books_by_author(author_id)
        print(f"Books by author with ID {author_id}:")
        for book in books_by_author:
            print(f"  - {book.title}")
    except Author.DoesNotExist:
        print(f"Author with ID {author_id} not found.")
    except Exception as e:
        print(f"Error: {e}")
    
    print()
    
    # Example 2: List all books in a library
    print("=" * 60)
    print("Example 2: List all books in a library")
    print("=" * 60)
    try:
        library_id = 1
        books_in_library = query_books_in_library(library_id)
        print(f"Books in library with ID {library_id}:")
        for book in books_in_library:
            print(f"  - {book.title} by {book.author.name}")
    except Library.DoesNotExist:
        print(f"Library with ID {library_id} not found.")
    except Exception as e:
        print(f"Error: {e}")
    
    print()
    
    # Example 3: Retrieve the librarian for a library
    print("=" * 60)
    print("Example 3: Retrieve the librarian for a library")
    print("=" * 60)
    try:
        library_id = 1
        librarian = query_librarian_for_library(library_id)
        print(f"Librarian for library with ID {library_id}:")
        print(f"  - Name: {librarian.name}")
        print(f"  - Library: {librarian.library.name}")
    except Librarian.DoesNotExist:
        print(f"No librarian found for library with ID {library_id}.")
    except Library.DoesNotExist:
        print(f"Library with ID {library_id} not found.")
    except Exception as e:
        print(f"Error: {e}")
