from django import forms
from .models import applicants



class ApplyForm(forms.ModelForm):
    class Meta:
        model=applicants
        fields=['name','Email','website','cv','coverLetter']
