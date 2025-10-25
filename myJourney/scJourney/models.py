# Import the Django models module to create database models
from django.db import models

class AboutMe(models.Model):
   
    name = models.CharField(max_length=100, help_text="Enter your full name")
    bio = models.TextField(help_text="Write a brief biography about yourself")
    email = models.EmailField(help_text="Enter your email address")

    def __str__(self):
        """String representation of the AboutMe object"""
        return self.name

    class Meta:
         # Customize how the model name appears in the admin panel
        verbose_name = "Personal Information"
        verbose_name_plural = "Personal Information"


class LearningJourney(models.Model):
   
    title = models.CharField(max_length=200, help_text="Title of your learning milestone")
    description = models.TextField(help_text="Describe what you learned and how it helped you")
    date = models.DateField(auto_now_add=True, help_text="Date when this milestone was added")

    def __str__(self):
        """String representation of the LearningJourney object"""
        return self.title

    class Meta:
         # Customize names shown in the admin panel
        verbose_name = "Learning Milestone"
        verbose_name_plural = "Learning Milestones"
             # Display the most recent milestones first
        ordering = ['-date']  # Order by most recent first

