from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

# Author Model
class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
# Book Model
class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    
    class Meta:
        permissions = [
            ("can_add_book", "Can Add Books In This Library"),
            ("can_change_book", "Can Change this books in Library"),
            ("can_delete_book", "Can Delete Books In Library"),
        ]
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
# Library Model
class Library(models.Model):
    name = models.CharField(max_length=30)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name
    
# Librarian Model
class Librarian(models.Model):
    name = models.CharField(max_length=30)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
# UserProfile Model
class UserProfile(models.Model):
    ROLES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member')
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, choices=ROLES, null=True, blank=True)

    def __str__(self):
        return f"{self.user} with role {self.role}"
 
# Auto-create user profile for new users
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance, role='Member')
        
# Save user profile when updated
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'userprofile'):
        instance.userprofile.save()