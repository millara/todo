from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.views.generic import ListView
from mainapp.models import Job


app_name = 'mainapp'
urlpatterns = [
    url(r'^jobs/$', views.JobList.as_view(), name='jobs'),
    #url(r'^create_job/', views.JobCreateView.as_view(), name='create-job'),
    url(r'^job_create/', views.job_create, name='job-create'), #function view
    url(r'^delete_job/(?P<pk>\d+)/$', views.JobDelete.as_view(), name='delete-job'),    url(r'^job_deleted/', views.JobDelete.as_view(), name="job-deleted"),
    url(r'^$', views.home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
