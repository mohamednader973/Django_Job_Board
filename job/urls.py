from django.urls import path,include

from .import views

app_name='job'

urlpatterns = [
    path('', views.Job_list),
    path('<str:slug>', views.Job_detail,name='job_detail'),
]
