from django.contrib import admin

# Register your models here.
from .models import Userprofile,city

admin.site.register(Userprofile)
admin.site.register(city)
