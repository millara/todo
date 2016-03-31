from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
# Change your models (in models.py).
# Run python manage.py makemigrations to create migrations for those changes
# Run python manage.py migrate to apply those changes to the database.
# Create your models here.


class Job(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateField(default=timezone.now)
    finish_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

    #def days_left(self):
        #return (self.finish_date - self.start_date).days
