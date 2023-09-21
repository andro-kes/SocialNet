from django.urls import path
from . import views

urlpatterns = [
    path('_<slug:slug>', views.ProfileView.as_view(), name='profile'),
    path('', views.CreateProfileView.as_view(), name='create_profile'),
    path('_update/<slug:slug>', views.UpdateProfileView.as_view(), name='update_profile'),
]
