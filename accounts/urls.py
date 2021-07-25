from django.urls import path
from accounts import views

urlpatterns = [
  path('profile/', views.ProfileView, name='profile'),
  path('profile/edit/', views.ProfileEditView, name='profile_edit'),
  path('login/', views.LoginView, name='account_login'),
  path('logout/', views.LogoutView, name='account_logout'),
  path('signup/', views.SignupView, name='account_signup'),
]
