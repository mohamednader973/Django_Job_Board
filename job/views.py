from django.shortcuts import render
from .models import job

# Create your views here.


def Job_list(request):
    Job_list=job.objects.all()
    context={'jobs':Job_list}
    return render(request,'jobs/jobs_list.html',context)


def Job_detail(request,id):
    Job_detail=job.objects.get(id=id)
    context={'job':Job_detail}
    return render(request,'jobs/job_details.html',context)