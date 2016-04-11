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



class JobList(ListView):
    model = Job


class JobDelete(DeleteView):
    model = Job
    def get_success_url(self):
        return reverse('mainapp:jobs')


def job_create(request):
    args = {}
    if request.method == 'POST':
        form = CreateJobForm(request.POST)
        if form.is_valid():
            form.clean_dates()
            # https://docs.djangoproject.com/en/1.9/topics/forms/#field-data
            form.save()
            return HttpResponseRedirect(reverse('mainapp:jobs'))
    #else:
        # validation is required, empty title field causes error
    else:
        form = CreateJobForm()
    args['form'] = form
    #context = {'form': form}
    return render(request, 'mainapp/job_form.html', args)


def home(request):
    hello = "hello view"
    return HttpResponse(hello)