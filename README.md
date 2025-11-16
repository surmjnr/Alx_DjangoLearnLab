# LibraryProject

This is a minimal Django project created for the ALX Django learning lab.

How to run locally:

1. Create a virtual environment and activate it:
	- Windows (PowerShell):
	  ```powershell
	  python -m venv venv
	  .\venv\Scripts\Activate.ps1
	  ```
2. Install Django:
	```powershell
	pip install django
	```
3. Navigate to the project folder and run the development server:
	```powershell
	cd LibraryProject
	python manage.py runserver
	```
4. Open http://127.0.0.1:8000/ in your browser to view the Django welcome page.

Project structure highlights:
- `manage.py` : Django's command-line utility
- `LibraryProject/settings.py` : Project settings
- `LibraryProject/urls.py` : URL declarations

This README was added to satisfy repository checks that require a non-empty `README.md`.
