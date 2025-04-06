from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUserModel


# Define the ModelAdmin class
class CustomUserAdmin(UserAdmin):
    model = CustomUserModel
    list_display = ('username', 'email', 'is_staff', 'date_of_birth', 'profile_photo')
    
    list_filter = ('is_staff', 'is_active', 'date_of_birth')

    search_fields = ('username', 'email')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'date_of_birth', 'profile_photo')
        }),
    )

# Register the CustomUserModel with the CustomUserAdmin
admin.site.register(CustomUserModel, CustomUserAdmin)