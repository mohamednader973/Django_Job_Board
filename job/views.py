from django.shortcuts import render,redirect
from .models import job,applicants
from django.core.paginator import Paginator
from .forms import ApplyForm,AddJob
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.


def Job_list(request):
    Job_list=job.objects.all()
    paginator = Paginator(Job_list, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context={'jobs':page_obj}
    return render(request,'jobs/jobs_list.html',context)





def Job_detail(request,slug):
    Job_detail=job.objects.get(slug=slug)
    if (request.method=='POST'):
        form=ApplyForm(request.POST,request.FILES)
        if form.is_valid():
            #form=ApplyForm(file_filed=request.FILES["file"])
            myform=form.save(commit=False)
            myform.job=Job_detail
            myform.save()

    else:
        form=ApplyForm()
    context={'job':Job_detail,'form':form}
    return render(request,'jobs/job_details.html',context)


@login_required
def add_job(request):
    if (request.method=='POST'):
        form=AddJob(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.author=request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form=AddJob()

    return render(request,'jobs/add_job.html',{'form':form})
