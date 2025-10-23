"""
Django Views for Personal Learning Journey Web Application
Author: Sonam Choden
Student ID: 08230193
Lab: 04 - Django MVT Architecture

This module contains the view functions that handle HTTP requests
and return appropriate responses for the learning journey application.
"""

from django.shortcuts import render
from .models import AboutMe, LearningJourney

def Index(request):
    """
    View function for the main learning journey page.
    
    This view retrieves all learning journey entries from the database
    and passes them to the Index.html template for display.
    
    Args:
        request: HTTP request object
        
    Returns:
        HttpResponse: Rendered Index.html template with journey data
    """
    # Retrieve all learning journey entries from the database
    journeys = LearningJourney.objects.all()
    
    # Render the Index template with the journey data
    return render(request, 'Index.html', {'journeys': journeys})


def aboutMe(request):
    """
    View function for the 'About Me' page.
    
    This view retrieves the first (and typically only) AboutMe entry
    from the database and passes it to the aboutMe.html template.
    
    Args:
        request: HTTP request object
        
    Returns:
        HttpResponse: Rendered aboutMe.html template with personal data
    """
    # Retrieve the first (and typically only) personal information entry
    about = AboutMe.objects.first()
    
    # Render the aboutMe template with the personal data
    return render(request, 'aboutMe.html', {'about': about})

