# DELETE Operation - Book Model

## Command
```python
retrieved_book.delete()
remaining_books = Book.objects.all()
print(f"Remaining books: {list(remaining_books)}")
print(f"Total books: {remaining_books.count()}")
```

## Expected Output
```
# Book with ID 1 deleted successfully
# Verification: Remaining books in database: []
# Total books after deletion: 0
```

## Description
This command deletes the Book instance with ID 1 from the database. The process involves:

1. **Call delete()**: Execute `retrieved_book.delete()` to remove the book from the database
2. **Verify deletion**: Query all remaining books using `Book.objects.all()`
3. **Confirm empty state**: Check that the count is 0, confirming the deletion

## Result
The Book instance is successfully deleted from the database. The verification shows an empty QuerySet, confirming that no books remain in the database after the deletion. This demonstrates that the DELETE operation was successful and the book record has been permanently removed from the database.
