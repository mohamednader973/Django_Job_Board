from django import forms
from .models import applicants
from .models import job



class ApplyForm(forms.ModelForm):
    class Meta:
        model=applicants
        fields=['name','Email','website','cv','coverLetter']

class AddJob(forms.ModelForm):
    class Meta:
        model=job
        fields='__all__'
        exclude=('slug','author')
