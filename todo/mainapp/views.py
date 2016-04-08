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


class JobDelete(DeleteView):
    model = Job
    def get_success_url(self):
        return reverse('mainapp:jobs')


# class JobCreateView(CreateView):
#     form_class = CreateJobForm
#     model = Job
#     success_url="/mainapp/jobs"


def job_create(request):
    
    if request.method == 'POST':
        form = CreateJobForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('mainapp:jobs'))
        else:
            return HttpResponse('Error')
    form = CreateJobForm()
    context = {'form': form}
    return render(request, 'mainapp/job_form.html', context)


def home(request):
    hello = "hello view"
    return HttpResponse(hello)