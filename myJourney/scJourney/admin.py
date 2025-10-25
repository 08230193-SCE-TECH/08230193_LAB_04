
#The first line allows you to use Django’s admin features
from django.contrib import admin
# Import the models from the current app
from .models import AboutMe, LearningJourney

# Register your models here.

# Register AboutMe model in admin interface
admin.site.register(AboutMe)

# Register LearningJourney model in admin interface
admin.site.register(LearningJourney)

