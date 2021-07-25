from django.shortcuts import render, redirect
from django.views import View
from accounts.models import CustomUser
from accounts.forms import ProfileForm, SignupUserForm
from allauth.account import views


class ProfileView(View):
  def get(self, request, *args, **kwargs):
    user_data = CustomUser.objects.get(id=request.user.id)
    return render(request, 'accounts/profile.html',{
      'user_data': user_data
    })

ProfileView = ProfileView.as_view()

class ProfileEditView(View):
  def get(self, request, *args, **kwargs):
    user_data = CustomUser.objects.get(id=request.user.id)
    form = ProfileForm(
      request.POST or None,
      initial = {
        'first_name': user_data.first_name,
        'last_name': user_data.last_name,
      }
    )

    return render(request, 'accounts/profile_edit.html',{
      'form': form
    })

  def post(self, request, *args, **kwargs):
    form = ProfileForm(request.POST or None)
    if form.is_valid():
      user_data = CustomUser.objects.get(id=request.user.id)
      user_data.first_name = form.cleaned_data['first_name']
      user_data.last_name = form.cleaned_data['last_name']
      user_data.save()
      return redirect('profile')

    return render(request, 'accounts/profile.html', {
      'form': form
    })

ProfileEditView = ProfileEditView.as_view() 

class LoginView(views.LoginView):
  template_name = 'accounts/login.html'

LoginView = LoginView.as_view()

class LogoutView(views.LogoutView):
  template_name = 'accounts/logout.html'

  def post(self, *args, **kwargs):
    if self.request.user.is_authenticated:
      self.logout()
    return redirect('home')

LogoutView = LogoutView.as_view()


class SignupView(views.SignupView):
  template_name = 'accounts/signup.html'
  
  def save(self, request):
    user = super(SignupUserForm, self).save(request)
    user.first_name = self.cleaned_data['first_name']
    user.last_name = self.cleaned_data['last_name']
    user.save()
    return user

SignupView = SignupView.as_view()