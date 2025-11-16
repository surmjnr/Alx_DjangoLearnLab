# CRUD Operations Documentation - Book Model

## Overview
This document contains comprehensive documentation of all CRUD (Create, Read, Update, Delete) operations performed on the Book model in the Django bookshelf application.

---

## 1. CREATE Operation

**Command:**
```python
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
```

**Output:**
```
Book created successfully with ID 1
- Title: 1984
- Author: George Orwell
- Publication Year: 1949
```

**Description:**
Creates a new Book instance in the database with the specified attributes. The `create()` method is a shorthand for instantiating and saving an object in one call.

---

## 2. RETRIEVE Operation

**Command:**
```python
retrieved_book = Book.objects.get(id=1)
```

**Output:**
```
Book retrieved successfully
- Title: 1984
- Author: George Orwell
- Publication Year: 1949
- ID: 1
```

**Description:**
Retrieves the Book instance with ID 1 from the database using the `get()` method. All attributes of the book are displayed to confirm successful retrieval.

---

## 3. UPDATE Operation

**Command:**
```python
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
```

**Output:**
```
Book updated successfully
Verification: Title is now 'Nineteen Eighty-Four'
```

**Description:**
Updates the title of the Book instance from "1984" to "Nineteen Eighty-Four" and saves the changes to the database using the `save()` method. The update is immediately persisted.

---

## 4. DELETE Operation

**Command:**
```python
retrieved_book.delete()
remaining_books = Book.objects.all()
```

**Output:**
```
Book with ID 1 deleted successfully
Verification: Remaining books in database: []
Total books after deletion: 0
```

**Description:**
Deletes the Book instance from the database. Verification confirms that no books remain, demonstrating successful deletion.

---

## Summary

| Operation | Status | Details |
|-----------|--------|---------|
| CREATE | ✓ Success | Book "1984" created with ID 1 |
| RETRIEVE | ✓ Success | Book retrieved with all attributes |
| UPDATE | ✓ Success | Title updated to "Nineteen Eighty-Four" |
| DELETE | ✓ Success | Book deleted, database is empty |

All CRUD operations have been successfully executed and documented.

---

## Model Definition

**File:** `bookshelf/models.py`

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title
```

---

## Migration Information

**Migration File:** `bookshelf/migrations/0001_initial.py`

- Creates the `bookshelf_book` table in the database
- Defines the following columns:
  - `id` (Primary Key, Auto-increment)
  - `title` (VARCHAR, max_length=200)
  - `author` (VARCHAR, max_length=100)
  - `publication_year` (INTEGER)

**Migration Commands Executed:**
```bash
python manage.py makemigrations bookshelf
python manage.py migrate
```

---

## Database Details

- **Database Engine:** SQLite (default Django database)
- **Database File:** `db.sqlite3`
- **Bookshelf App Registration:** Added to `INSTALLED_APPS` in `settings.py`

