# Generated by Django 5.1.3 on 2024-12-14 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0004_alter_userprofile_role'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': (('can_add_book', 'Can Add Books In This Library'), ('can_change_book', 'Can Change this books in Library'), ('can_delete_book', 'Can Delete Books In Library'))},
        ),
    ]
