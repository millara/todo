from django import forms
import datetime
from .models import Job
from django.forms.extras.widgets import SelectDateWidget


class CreateJobForm(forms.ModelForm):
    #start_date = forms.DateField(initial=datetime.date.today())
    finish_date = forms.DateField(initial=datetime.date.today(),
                                  widget=SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"),),)
    title = forms.CharField(initial='Title',)

    class Meta:
        model = Job
        #fields = ['title', 'finish_date',]
        exclude = ['start_date']
        #widgets = {'finish_date': forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"),)}

    #https://docs.djangoproject.com/en/1.9/ref/forms/validation/#cleaning-a-specific-field-attribute
    def clean(self):
        #start  = self.cleaned_data['start_date']
        finish = self.cleaned_data['finish_date']
        if finish < datetime.date.today():
            raise forms.ValidationError('The finish date must be in the future', code='invalid finish date')
        return finish

