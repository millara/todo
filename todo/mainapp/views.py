from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
import datetime
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import DeleteView  # this is the generic view
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import ListView, CreateView
from .models import Job
from .forms import CreateJobForm
from .forms import AddJobForm


class JobList(ListView):
    model = Job


class JobCreateView(CreateView):
    model = Job
    fields = ['title', 'start_date', 'finish_date']
    success_url="/mainapp/jobs"
    #template_name = "job_create_form.html"


class JobDelete(DeleteView):
    model = Job
    def get_success_url(self):
        return reverse('mainapp:jobs')


def home(request):
    hello = "hello view"
    return HttpResponse(hello)