from django.urls import path,include
from .import views

app_name='accounts'

urlpatterns = [
    path('signup', views.signup,name='sign_up'),
    path('profile', views.prof,name='profile'),
    path('profile/edit', views.profileEdit,name='profile_edit'),
]
