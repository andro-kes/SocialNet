from django.urls import path
from . import views

urlpatterns = [
    path('', views.CreatePostView.as_view(), name='create_post'),
    path('detail/<int:pk>', views.DetailPostView.as_view(), name='detail_post'),
]
