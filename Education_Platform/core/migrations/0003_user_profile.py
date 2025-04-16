# Generated by Django 5.2 on 2025-04-16 15:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_category_course_average_rating_course_lessons_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Profile',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to='core.profile'),
        ),
    ]
