from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload, name='upload'),
    path('detail/<int:pk>/', views.Detail.as_view(), name='detail'),
    path('delete/<int:pk>/', views.Delete.as_view(), name='delete'),
]