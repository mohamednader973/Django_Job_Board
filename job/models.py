from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


# Create your models here.
Job_type=(
    ("Part time","Part time"),
    ("full time","full time")
)

def image_upload_name(instance,image_name):
    imgName,ext=image_name.split(".")
    return "jobs/%s.%s"%(instance.id,ext)


class job(models.Model):
    title=models.CharField(max_length=100)
    author=models.ForeignKey(User,related_name="job_owner",on_delete=models.CASCADE)
    job_type=models.CharField(max_length=15,choices=Job_type)
    description=models.TextField(max_length=1000)
    published_At=models.DateTimeField(auto_now=True)
    vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    experience=models.IntegerField(default=1)
    category=models.ForeignKey('category',on_delete=models.CASCADE)
    img=models.ImageField(upload_to=image_upload_name)
    slug=models.SlugField(blank=True,null=True)


    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(job,self).save(*args,**kwargs)

    def __str__(self):
        return self.title


class category(models.Model):
    name=models.CharField(max_length=25)
    def __str__(self):
        return self.name

def file_upload_name(instance,file_name):
    filName,ext=file_name.split(".")

    app=applicants.objects.latest('id').id

    return "applicants/%s.%s"%(app+1,ext)



class applicants(models.Model):
    name=models.CharField(max_length=100)
    job=models.ForeignKey(job,related_name="applied_Job",on_delete=models.CASCADE)
    Email=models.EmailField(max_length=50)
    website=models.URLField()
    cv=models.FileField(upload_to=file_upload_name)
    coverLetter=models.TextField(max_length=500)
    uploaded_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
