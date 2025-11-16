# RETRIEVE Operation - Book Model

## Command
```python
retrieved_book = Book.objects.get(id=1)
print(f"Title: {retrieved_book.title}")
print(f"Author: {retrieved_book.author}")
print(f"Publication Year: {retrieved_book.publication_year}")
print(f"ID: {retrieved_book.id}")
```

## Expected Output
```
# Title: 1984
# Author: George Orwell
# Publication Year: 1949
# ID: 1
```

## Description
This command retrieves the Book instance with ID 1 from the database using the `get()` method. Once retrieved, all attributes of the book are displayed:
- **ID**: 1 (primary key)
- **Title**: "1984"
- **Author**: "George Orwell"
- **Publication Year**: 1949

## Result
The Book instance is successfully retrieved from the database with all its attributes intact and accessible.
