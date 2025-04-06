from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.

# Custom User Model.
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)


# Author Model.
class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
# Book Model.
class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    class Meta:
        permissions = [
            ("can_add_book","Can Add Books In This Library"),
            ("can_change_book","Can Change this books in Library"),
            ("can_delete_book","Can Delete Books In Library"),
        ]
    def __str__(self):
        return f"{self.title} by {self.author}"
    
# Library Model.
class Library(models.Model):
    name = models.CharField(max_length=30)
    books = models.ManyToManyField(Book, related_name='librares')

    def __str__(self):
        return self.name
    
# Librarian Model.
class Librarian(models.Model):
    name = models.CharField(max_length=30)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
# Task03

# # Class UserProfile.
# class UserProfile(models.Model):
#     ROLES =  [
#         ('Admin', 'Admin'),
#         ('Librarian', 'Librarian'),
#         ('Member', 'Member')
#     ]
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     role = models.CharField(max_length=100, choices=ROLES, null=True, blank=True)

#     def __str__(self):
#         return f"{self.user} with role {self.role}"
 
# # function for auto create user profile for users already exists   
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance, role='Member')
        
# # function for save user profile whene created
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     if hasattr(instance, 'userprofile'):
#         instance.userpofile.save()
        
    

