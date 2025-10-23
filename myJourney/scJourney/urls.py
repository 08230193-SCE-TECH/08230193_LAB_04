"""
URL Configuration for Personal Learning Journey Web Application
Author: Sonam Choden
Student ID: 08230193
Lab: 04 - Django MVT Architecture

This module defines the URL patterns for the scJourney app.
It maps URLs to their corresponding view functions.
"""

from django.urls import path
from . import views

# URL patterns for the learning journey application
urlpatterns = [
    # Main learning journey page (homepage)
    path('', views.Index, name='Index'),
    
    # About Me page
    path('about/', views.aboutMe, name='aboutMe'),
]