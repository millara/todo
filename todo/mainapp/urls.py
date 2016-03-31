from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'mainapp'
urlpatterns = [
    url(r'^add_job/', views.job_create, name='add job'),
    url(r'^display_jobs/', views.display_jobs, name='display-jobs'),
    url(r'^create_job/', views.create_job_test, name='create job'),
    url(r'^delete_job/(?P<pk>\d+)/$', views.JobDelete.as_view(), name="delete_job"),
    url(r'^job_deleted/', views.JobDelete.as_view(), name="job deleted"),
    url(r'^$', views.home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
