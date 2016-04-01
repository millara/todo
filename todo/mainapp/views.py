from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
import datetime
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import DeleteView  # this is the generic view
from django.core.urlresolvers import reverse_lazy
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


def home(request):
    hello = "hello view"
    return HttpResponse(hello)


def job_create(request):
    form = AddJobForm()
    context = {
        "form": form,
    }
    return render(request, "add_job_form.html", context)


# def create_job(request):
#     temp_var = [0, 1, 2, 3, 4, 5]
#     template = loader.get_template('mainapp/todolist.html')
#     context = {'temp_var': temp_var}
#     return HttpResponse(template.render(context, request))


@csrf_protect
def create_job_test(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        job = Job()

        form = CreateJobForm(request.POST, instance=job)

        if form.isvalid():
            # process the data in form.cleaned_data as required.
            # if is_valid() is True, we’ll now be able to find all
            # the validated form data in its cleaned_data attribute.
            # We can use this data to update the database or do
            # other processing before sending an HTTP redirect to
            # the browser telling it where to go next.
            # redirect to a new URL:

            job.save()

            # return HttpResponseRedirect('/display_jobs/')
            return render(request, 'create_job.html', {'form: form'})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = CreateJobForm()

    return render(request, 'mainapp/create_job.html', {'form': form})



# def display_jobs(request):
#     # get list of jobs then display them
#     # if request == POST???? do i need to do this like in the create
#     # job test function above in order to save the data?
#     if request.method == "POST":
#         form = AddJobForm(request.POST)
#         if form.is_valid():
#             form.save(commit=True)
#         else:
#             print(form.errors)

#     job_list = Job.objects.all()
#     template = loader.get_template('display_jobs.html')
#     context = {'job_list': job_list}
#     return HttpResponse(template.render(context, request))


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

# Subclass the generic DeleteViewleteView
class JobDelete(DeleteView):
    model = Job
    success_url = reverse_lazy('display-jobs')
    template_name = 'delete_job.html'
