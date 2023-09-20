from django.shortcuts import render
from .models import job,applicants
from django.core.paginator import Paginator
from .forms import ApplyForm
from django.http import HttpResponseRedirect


# Create your views here.


def Job_list(request):
    Job_list=job.objects.all()
    paginator = Paginator(Job_list, 1)
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
