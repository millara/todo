from django import forms
import datetime
from .models import Job
from django.forms.extras.widgets import SelectDateWidget

# class CreateJobForm(forms.Form):
#     job_title = forms.CharField(label='Job Title', max_length=100)

class CreateJobForm(forms.ModelForm):
    start_date = forms.DateField(widget=SelectDateWidget(empty_label="Nothing"))
    finish_date = forms.DateField(widget=SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"),),)
    class Meta:
        model = Job
        fields = ['title', 'start_date', 'finish_date']
        #widgets = {'date': DateInput(attrs={'class': 'datepicker'})}

class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
