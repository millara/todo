from django.shortcuts import redirect, render, get_list_or_404, get_object_or_404
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
    # days_left = days_left()


def job_update(request, pk, template_name='mainapp/job_form.html'):
    job = get_object_or_404(Job, pk=pk)
    form = CreateJobForm(request.POST or None, instance=job)
    if form.is_valid():
        form.save()
        return redirect('mainapp:jobs')
    return render(request, template_name, {'form':form})

# def job_list(request):
#     jobs = jobs.objects.all()
#     context = {
#         'jobs': jobs
#     }
#     return render(request, 'mainapp/job_list.html', context)


class JobDelete(DeleteView):
    model = Job
    def get_success_url(self):
        return reverse('mainapp:jobs')


def job_create(request):
    args = {}
    if request.method == 'POST':
        form = CreateJobForm(request.POST)
        if form.is_valid():
            # https://docs.djangoproject.com/en/1.9/topics/forms/#field-data
            form.save()
            return HttpResponseRedirect(reverse('mainapp:jobs'))
    # validation is required, empty title field causes error
    else:
        form = CreateJobForm()
    args['form'] = form
    return render(request, 'mainapp/job_form.html', args)

def days_left(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

def home(request):
    hello = "hello view"
    return HttpResponse(hello)