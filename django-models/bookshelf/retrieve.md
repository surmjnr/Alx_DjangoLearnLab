# RETRIEVE Operation - Book Model

## Command
```
retrieved_book = Book.objects.get(id=1)
print(f"Title: {retrieved_book.title}")
print(f"Author: {retrieved_book.author}")
print(f"Publication Year: {retrieved_book.publication_year}")
```

## Output
```
# Title: 1984
# Author: George Orwell
# Publication Year: 1949
# ID: 1
```
