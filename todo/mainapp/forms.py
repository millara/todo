from django import forms

from .models import Job


class CreateJobForm(forms.Form):
    job_title = forms.CharField(label='Job Title', max_length=100)


class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
