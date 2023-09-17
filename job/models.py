from django.db import models

# Create your models here.
Job_type=(
    ("Part time","Part time"),
    ("full time","full time")
)
    
    

class job(models.Model):
    title=models.CharField(max_length=100)
    job_type=models.CharField(max_length=15,choices=Job_type)
