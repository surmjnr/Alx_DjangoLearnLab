# CREATE Operation - Book Model

## Command
```python
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
```

## Expected Output
```
# Output: Book created successfully with ID 1
# - Title: 1984
# - Author: George Orwell
# - Publication Year: 1949
```

## Description
This command creates a new Book instance with the following attributes:
- **Title**: "1984"
- **Author**: "George Orwell"
- **Publication Year**: 1949

The `create()` method performs both the object creation and database insertion in a single operation, returning the created Book instance. The book is assigned an auto-generated primary key ID of 1.

## Result
The Book instance is successfully created and saved to the database.
