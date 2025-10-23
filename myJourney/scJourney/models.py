"""
Django Models for Personal Learning Journey Web Application
Author: Sonam Choden
Student ID: 08230193
Lab: 04 - Django MVT Architecture

This module defines the data models for the learning journey application.
It includes models for personal information and learning milestones.
"""

from django.db import models

class AboutMe(models.Model):
    """
    Model to store personal information about the student.
    
    Fields:
        name (CharField): Full name of the student
        bio (TextField): Personal biography and background information
        email (EmailField): Contact email address
    
    This model represents the 'About Me' section of the website.
    """
    name = models.CharField(max_length=100, help_text="Enter your full name")
    bio = models.TextField(help_text="Write a brief biography about yourself")
    email = models.EmailField(help_text="Enter your email address")

    def __str__(self):
        """String representation of the AboutMe object"""
        return self.name

    class Meta:
        verbose_name = "Personal Information"
        verbose_name_plural = "Personal Information"


class LearningJourney(models.Model):
    """
    Model to store learning milestones and achievements.
    
    Fields:
        title (CharField): Title of the learning milestone
        description (TextField): Detailed description of what was learned
        date (DateField): Date when the milestone was added (auto-generated)
    
    This model represents individual learning achievements in the journey.
    """
    title = models.CharField(max_length=200, help_text="Title of your learning milestone")
    description = models.TextField(help_text="Describe what you learned and how it helped you")
    date = models.DateField(auto_now_add=True, help_text="Date when this milestone was added")

    def __str__(self):
        """String representation of the LearningJourney object"""
        return self.title

    class Meta:
        verbose_name = "Learning Milestone"
        verbose_name_plural = "Learning Milestones"
        ordering = ['-date']  # Order by most recent first

