from django.db import models

# Create your models here.
Job_type=(
    ("Part time","Part time"),
    ("full time","full time")
)
    
    

class job(models.Model):
    title=models.CharField(max_length=100)
    job_type=models.CharField(max_length=15,choices=Job_type)
    description=models.TextField(max_length=1000)
    published_At=models.DateTimeField(auto_now=True)
    vacancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    experience=models.IntegerField(default=1)
    category=models.ForeignKey('category',on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    

class category(models.Model):
    name=models.CharField(max_length=25)
    def __str__(self):
        return self.name

