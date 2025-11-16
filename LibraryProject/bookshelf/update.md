# UPDATE Operation - Book Model

## Command
```python
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
print(f"Updated title: {retrieved_book.title}")
```

## Expected Output
```
# Book updated successfully
# Updated title: Nineteen Eighty-Four
```

## Description
This command updates the title of the Book instance from "1984" to "Nineteen Eighty-Four". The process involves:

1. **Modify the attribute**: Set `retrieved_book.title = "Nineteen Eighty-Four"`
2. **Save to database**: Call `retrieved_book.save()` to persist the changes
3. **Verify the change**: Access the updated title to confirm the modification

## Result
The Book's title is successfully updated from "1984" to "Nineteen Eighty-Four" in the database. The `save()` method persists the change, ensuring it is reflected in the database immediately.
