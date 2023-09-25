from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

def image_upload_name(instance,image_name):
    imgName,ext=image_name.split(".")
    return "users/%s.%s"%(instance.id,ext)

class Userprofile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number=models.CharField(max_length=15)
    img=models.ImageField(upload_to=image_upload_name)
    city=models.ForeignKey('city',related_name="user_city",on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)


class city(models.Model):
    city=models.CharField(max_length=30)
    def __str__(self):
        return self.city
