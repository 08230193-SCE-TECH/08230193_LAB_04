"""
Django Admin Configuration for Personal Learning Journey Web Application
Author: Sonam Choden
Student ID: 08230193
Lab: 04 - Django MVT Architecture

This module configures the Django admin interface for managing
the learning journey application data.
"""

from django.contrib import admin
from .models import AboutMe, LearningJourney

# Register your models here.

# Register AboutMe model in admin interface
admin.site.register(AboutMe)

# Register LearningJourney model in admin interface
admin.site.register(LearningJourney)

