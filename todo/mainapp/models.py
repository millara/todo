from django.db import models
import datetime
from django.utils import timezone
from django.core.urlresolvers import reverse
# Create your models here.
# Change your models (in models.py).
# Run python manage.py makemigrations to create migrations for those changes
# Run python manage.py migrate to apply those changes to the database.


class Job(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateField(auto_now_add = True)
    finish_date = models.DateField(default=timezone.now)
    
    class Meta:
        ordering = ['finish_date']

    @property
    def days_left(self):
        return ( self.finish_date - datetime.date.today() ).days 
 

    # def __str__(self):
    #     return self.title