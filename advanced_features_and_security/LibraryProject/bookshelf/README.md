# How to Create and Activate Permissions in the Book Model in Django

In this file, we will explain step-by-step how to create custom permissions for the `Book` model in a Django application and activate them for use in your project. We assume the app is named `bookshelf`.

---

## Step 1: Define the Model with Custom Permissions
First, define the `Book` model in the `models.py` file within the `bookshelf` app, adding custom permissions using the `Meta` class.

### Example:
```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    class Meta:
        permissions = [
            ('can_view', 'Can view book'),
            ('can_create', 'Can create book'),
            ('can_edit', 'Can edit book'),
            ('can_delete', 'Can delete book'),
        ]
permissions: A list of tuples containing the codename (e.g., can_view) and a human-readable description (e.g., 'Can view book').

Step 2: Update the Database

After defining the permissions, you need to generate and apply migrations to add the model and its permissions to the database.
Commands:

    Generate migration files: 
        python manage.py makemigrations
    Apply the migrations:
        python manage.py migrate

    These commands will add the Book model and its permissions to database tables like auth_permission.



Step 3: Verify Permission Creation

You can verify that the permissions have been successfully added using the Django shell.
Example:

    Open the shell:
    bash

python manage.py shell
Run the following code:
python

    from django.contrib.auth.models import Permission
    from django.contrib.contenttypes.models import ContentType
    from bookshelf.models import Book

    content_type = ContentType.objects.get_for_model(Book)
    permissions = Permission.objects.filter(content_type=content_type)
    for perm in permissions:
        print(perm.codename, perm.name)

    Expected Output: Permissions like can_view, can_create, etc., will be displayed along with their descriptions.

Step 4: Assign Permissions to Users or Groups

You can assign permissions manually through the admin interface or programmatically.
A. Via the Admin Interface

    Ensure the model is registered in admin.py:
    python

from django.contrib import admin
from .models import Book

admin.site.register(Book)
Start the server:
bash

    python manage.py runserver
    Go to http://127.0.0.1:8000/admin/, log in as a superuser, and create a group or assign permissions directly to a user under the "Permissions" section.

B. Programmatically

You can assign permissions using Python code. Example:
python
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book

# Create a group
group, created = Group.objects.get_or_create(name='Book Editors')

# Get the content type
content_type = ContentType.objects.get_for_model(Book)

# Add permissions to the group
permissions = Permission.objects.filter(content_type=content_type)
for perm in permissions:
    group.permissions.add(perm)

# Add a user to the group
user = User.objects.get(username='your_username')
user.groups.add(group)


Step 5: Use Permissions in Views

Use the @permission_required decorator to check permissions in your views.
Example:
python
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book

@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

    bookshelf.can_view: Combines the app name (bookshelf) and the permission codename (can_view).


Step 6: Check Permissions in Templates

You can use the perms template tag to check permissions within templates.
Example:
html
{% if perms.bookshelf.can_create %}
    <a href="{% url 'book_create' %}" class="btn btn-primary">Add New Book</a>
{% endif %}
Additional Notes

    Create a Superuser: If you don’t have a user yet, create one with:
    bash

python manage.py createsuperuser
App Configuration: Ensure bookshelf is added to INSTALLED_APPS in settings.py:
python
INSTALLED_APPS = [
    ...
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'bookshelf',
]
Default Permissions: If you don’t define custom permissions, Django creates default ones like add_book, change_book, and delete_book.

---