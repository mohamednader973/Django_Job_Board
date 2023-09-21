from django.urls import path,include

from .import views

app_name='job'

urlpatterns = [
    path('', views.Job_list,name='job_list'),
    path('add', views.add_job,name='add_job'),
    path('<str:slug>', views.Job_detail,name='job_detail'),

]
