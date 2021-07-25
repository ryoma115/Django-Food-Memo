from django import forms
from allauth.account.forms import SignupForm


class ProfileForm(forms.Form):
  first_name = forms.CharField(max_length=30, label='姓')
  last_name = forms.CharField(max_length=30, label='名')


class SignupUserForm(SignupForm):
  first_name = forms.CharField(max_length=30, label='姓')
  last_name = forms.CharField(max_length=30, label='名')
