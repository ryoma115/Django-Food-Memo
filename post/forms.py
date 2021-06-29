from django import forms
from django.db.models import fields
from .models import Post

class DocumentForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('where', 'photo1', 'photo2', 'photo3', 'photo4', 'photo5', 'description')