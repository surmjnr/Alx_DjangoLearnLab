# Admin Setup for `Book` model

This file documents how the `Book` model is integrated into the Django admin and how to set up the environment to manage books through the admin interface.

What was added
- `LibraryProject/bookshelf/admin.py` now registers the `Book` model with a custom `ModelAdmin`:
  - `list_display`: shows `title`, `author`, and `publication_year` in the admin list view.
  - `list_filter`: filters by `author` and `publication_year`.
  - `search_fields`: enables search by `title` and `author`.

How to access the admin

1. Create and activate a virtual environment (PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

2. Install dependencies (if not already):

```powershell
pip install -r requirements.txt
```

3. Create a Django superuser (if you don't have one):

```powershell
cd LibraryProject
python manage.py createsuperuser
```

4. Run the development server and open the admin site:

```powershell
python manage.py runserver
# then open http://127.0.0.1:8000/admin/ in your browser
```

Notes on the admin configuration
- The `BookAdmin` configuration improves visibility and management of books in the admin list page.
- If you add more fields to `Book` (for example `genre` or `isbn`), consider adding them to `list_display` and `list_filter`.
- To change ordering or enable readonly fields, update `LibraryProject/bookshelf/admin.py` accordingly.

File locations
- Admin class: `LibraryProject/bookshelf/admin.py`
- Model: `LibraryProject/bookshelf/models.py`

Troubleshooting
- If you see import errors, ensure your Python environment is activated and dependencies installed.
- If admin changes don't appear, restart the development server.

--
Generated as part of the admin integration for the ALX Django learning lab.
